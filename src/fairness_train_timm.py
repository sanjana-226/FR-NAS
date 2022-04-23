from comet_ml import Experiment
import argparse
from tqdm import tqdm
import os
import torch
import torch.nn as nn
import torch.optim as optim
import yaml
from head.metrics import CosFace
from loss.focal import FocalLoss
from utils.utils import separate_resnet_bn_paras, warm_up_lr, load_checkpoint, \
    schedule_lr, AverageMeter, accuracy
from utils.fairness_utils import evaluate
from utils.data_utils_balanced import prepare_data
from utils.utils_train import Network
import numpy as np
import pandas as pd
import random
import timm
from utils.utils import save_output_from_dict
from utils.utils_train import Network, get_head
from utils.fairness_utils import evaluate, add_column_to_file
from timm.optim import create_optimizer_v2, optimizer_kwargs
from timm.scheduler import create_scheduler

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.manual_seed(222)
torch.cuda.manual_seed_all(222)
np.random.seed(222)
random.seed(222)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--config_path', type=str)

    args = parser.parse_args()
    with open(args.config_path, "r") as ymlfile:
        options = yaml.load(ymlfile, Loader=yaml.FullLoader)
        print(options)
    for key, value in options.items():
        setattr(args, key, value)
    if not os.path.isdir(
            os.path.join(
                args.checkpoints_root,
                args.backbone + '_' + args.head + '_' + args.opt)):
        os.mkdir(
            os.path.join(
                args.checkpoints_root,
                args.backbone + '_' + args.head + '_' + args.opt))
    p_images = {
        args.groups_to_modify[i]: args.p_images[i]
        for i in range(len(args.groups_to_modify))
    }
    p_identities = {
        args.groups_to_modify[i]: args.p_identities[i]
        for i in range(len(args.groups_to_modify))
    }
    args.p_images = p_images
    args.p_identities = p_identities

    print("P identities: {}".format(args.p_identities))
    print("P images: {}".format(args.p_images))

    ####################################################################################################################################
    # ======= data, model and test data =======#
    run_name = args.backbone + '_' + args.head + '_' + args.opt
    output_dir = os.path.join(args.checkpoints_root, run_name)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    experiment = Experiment(
        api_key=args.comet_api_key,
        project_name=args.project_name,
        workspace=args.comet_workspace,
    )
    experiment.add_tag(args.backbone)

    dataloaders, num_class, demographic_to_labels_train, demographic_to_labels_test = prepare_data(
        args)
    args.num_class = num_class
    ''' Model '''
    backbone = timm.create_model(args.backbone,
                                 num_classes=0,
                                 pretrained=args.pretrained,
                                 drop_rate=args.drop,
                                 drop_connect_rate=args.drop_connect,
                                 drop_path_rate=args.drop_path,
                                 drop_block_rate=args.drop_block,
                                 global_pool=args.gp,
                                 bn_momentum=args.bn_momentum,
                                 bn_eps=args.bn_eps,
                                 scriptable=args.torchscript,
                                 ).to(device)
    config = timm.data.resolve_data_config({}, model=backbone)
    model_input_size = args.input_size

    # get model's embedding size
    meta = pd.read_csv(args.metadata_file)
    embedding_size = int(
        meta[meta.model_name == args.backbone].feature_dim)
    args.embedding_size= embedding_size

    head = get_head(args)
    train_criterion = FocalLoss(elementwise=True)
    head,backbone= head.to(device), backbone.to(device)
    ####################################################################################################################
    # ======= argsimizer =======#
    model = Network(backbone, head)
   
    optimizer = create_optimizer_v2(model, **optimizer_kwargs(cfg=args))
    scheduler, num_epochs = create_scheduler(args, optimizer)

    model, argsimizer, epoch, batch, checkpoints_model_root = load_checkpoint(
        args, model, optimizer, dataloaders["train"], p_identities,
        p_images)
    model = nn.DataParallel(model)
    model = model.to(device)
    
    print('Start training')
    with experiment.train():
        while epoch <= args.epochs:

            experiment.log_current_epoch(epoch)
            model.train()  # set to training mode
            meters = {}
            meters["loss"] = AverageMeter()
            meters["top5"] = AverageMeter()

            #             if epoch in args.stages:  # adjust LR for each training stage after warm up, you can also choose to adjust LR manually (with slight modification) once plaueau observed
            #                 schedule_lr(argsimizer)

            for inputs, labels, sens_attr, _ in tqdm(iter(
                    dataloaders["train"])):

                #                 if batch + 1 <= num_batch_warm_up:  # adjust LR for each training batch during warm up
                #                     warm_up_lr(batch + 1, num_batch_warm_up, args.lr, argsimizer)

                inputs, labels = inputs.to(device), labels.to(device).long()
                outputs, reg_loss = model(inputs, labels)
                loss = train_criterion(outputs, labels) + reg_loss
                loss = loss.mean()
                argsimizer.zero_grad()
                loss.backward()
                argsimizer.step()
                scheduler.step(epoch + 1, meters["top5"])

                # measure accuracy and record loss
                prec1, prec5 = accuracy(outputs.data, labels, topk=(1, 5))
                meters["loss"].update(loss.data.item(), inputs.size(0))
                meters["top5"].update(prec5.data.item(), inputs.size(0))

                batch += 1

            backbone.eval()  # set to testing mode
            head.eval()
            experiment.log_metric("Training Loss",
                                  meters["loss"].avg,
                                  step=epoch)
            experiment.log_metric("Training Acc5",
                                  meters["top5"].avg,
                                  step=epoch)
            '''For train data compute only multilabel accuracy'''
            #             loss_train, acc_train, _, _, _, _,_,_,_,_ = evaluate(dataloaders.train, train_criterion, backbone,head, embedding_size,
            #                                                 k_accuracy = False, multilabel_accuracy = True,
            #                                                 demographic_to_labels = demographic_to_labels_train, test = False)
            '''For test data compute only k-neighbors accuracy and multi-accuracy'''
            k_accuracy = True
            multilabel_accuracy = True
            loss, acc, acc_k, predicted_all, intra, inter, angles_intra, angles_inter, correct, nearest_id, labels_all, indices_all, demographic_all = evaluate(
                dataloaders["test"],
                train_criterion,
                backbone,
                head,
                embedding_size,
                k_accuracy=k_accuracy,
                multilabel_accuracy=multilabel_accuracy,
                demographic_to_labels=demographic_to_labels_test,
                test=True)

            # save outputs
            # save outputs
            kacc_df, multi_df = None, None
            if k_accuracy:
                kacc_df = pd.DataFrame(np.array([list(indices_all),
                                                 list(nearest_id)]).T,
                                       columns=['ids','epoch_'+str(epoch)]).astype(int)
            if multilabel_accuracy:
                multi_df = pd.DataFrame(np.array([list(indices_all),
                                                  list(predicted_all)]).T,
                                        columns=['ids','epoch_'+str(epoch)]).astype(int)
            add_column_to_file(output_dir,
                               run_name, 
                               epoch,
                               multi_df = multi_df, 
                               kacc_df = kacc_df)
            results = {}
            results['Model'] = args.backbone
            results['seed'] = args.seed
            results['epoch'] = epoch
            for k in acc_k.keys():
                experiment.log_metric("Acc multi Test " + k, acc_k[k], epoch=epoch)
                experiment.log_metric("Acc k Test " + k, acc_k[k], epoch=epoch)
                experiment.log_metric("Intra Test " + k, intra[k], epoch=epoch)
                experiment.log_metric("Inter Test " + k, inter[k], epoch=epoch)

                results['Acc multi '+k] = (round(acc_k[k].item()*100, 3))
                results['Acc k '+k] = (round(acc_k[k].item()*100, 3))
                results['Intra '+k] = (round(intra[k], 3))
                results['Inter '+k] = (round(inter[k], 3))

            print(results)
            save_output_from_dict(args.out_dir, results, args.file_name)

            epoch += 1

            # save checkpoints per epoch

            if (epoch == args.epochs) or (epoch % args.save_freq == 0):
                checkpoint_name_to_save = os.path.join(
                    args.checkpoints_root,
                    args.backbone + '_' + args.head,
                    "Checkpoint_Head_{}_Backbone_{}_Dataset_{}_p_idx{}_p_img{}_Epoch_{}.pth"
                    .format(args.head, args.backbone, args.name,
                            str(args.p_identities), str(args.p_images),
                            str(epoch)))

                torch.save(
                    {
                        'epoch': epoch,
                        'model_state_dict': model.module.state_dict(),
                        'optimizer_state_dict': optimizer.state_dict()
                    }, checkpoint_name_to_save)
