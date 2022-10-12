#!/bin/bash
python src/create_all_configs.py --user_config config_user.yaml --backbone ghostnet_100 --lr 0.1 --momentum 0.9 --weight-decay 0.0001 --opt sgd --sched multistep --input_size 112
python src/create_all_configs.py --user_config config_user.yaml --backbone cspdarknet53 --lr 1e-4 --opt adam  --weight-decay 0.0005 --input_size 112
python src/create_all_configs.py --user_config config_user.yaml --backbone dpn107 --sched multistep --lr 0.001 --weight-decay 0.0001 --opt sgd --input_size 224
python src/create_all_configs.py --user_config config_user.yaml --backbone twins_svt_large --model-ema --input_size 112 --model-ema-decay 0.99996  --drop-path 0.1 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30  --min-lr 1e-5  --warmup-epochs 5 --batch_size 64
python src/create_all_configs.py --user_config config_user.yaml --backbone tf_efficientnet_b7 --sched step  --decay-epochs 2.4 --decay-rate .97 --input_size 112 --opt rmsproptf --opt-eps .001 --warmup-lr 1e-6 --weight-decay 1e-5 --drop 0.3 --drop-connect 0.2 --model-ema --model-ema-decay 0.9999  --lr .016
python src/create_all_configs.py --user_config config_user.yaml --backbone coat_lite_small --input_size 224 --drop-path 0.0  --model-ema --model-ema-decay 0.99996  --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30 --warmup-epochs 5 --batch_size 64
python src/create_all_configs.py --user_config config_user.yaml --backbone hrnet_w64 --opt sgd --lr 0.05 --weight-decay 0.0001 --input_size 224
python src/create_all_configs.py --user_config config_user.yaml --backbone jx_nest_base --batch_size 64 --lr 2.5e-4 --opt AdamW --weight-decay 0.05 --warmup-epoch 7 --input_size 224 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone visformer_small --batch_size 64 --lr 5e-4 --opt AdamW --weight-decay 0.05 --warmup-epoch 5 --opt-eps 1e-8 --warmup-lr 0.0001 --min-lr 1e-5 --input_size 224 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone swin_base_patch4_window7_224 --drop-path 0.5 --input_size 224 --model-ema --decay-epochs 30 --warmup-epochs 5 --weight-decay 1e-8 --lr 2e-05 --warmup-lr 2e-08 --min-lr 2e-07 --batch_size 64
python src/create_all_configs.py --user_config config_user.yaml --backbone convit_base --model-ema --input_size 224 --model-ema-decay 0.99996  --drop-path 0.1 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30 --min-lr 1e-5  --warmup-epochs 5 --batch_size 64
python src/create_all_configs.py --user_config config_user.yaml --backbone gluon_xception65 --batch_size 64 --lr 0.1 --warmup-epochs 5 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone xception65 --batch_size 64 --lr 0.1 --warmup-epochs 5 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone inception_resnet_v2 --batch_size 64 --lr 0.045 --lr-cycle-decay 0.94 --momentum 0.9 --opt RMSProp --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone rexnet_200 --batch_size 64 --lr 0.5 --momentum 0.9 --weight-decay 1e-5 --opt SGD --input_size 224 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone resnetrs101 --batch_size 64 --momentum 0.9 --lr 1.6 --opt SGD --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone vgg19_bn --batch_size 64 --lr 0.1 --momentum 0.9 --weight-decay 1e-4 --sched step --opt SGD --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone vgg19 --batch_size 64 --lr 0.01 --momentum 0.9 --weight-decay 1e-4 --sched step --opt SGD --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone tnt_s_patch16_224 --batch_size 64 --sched cosine --opt AdamW  --warmup-lr 1e-6 --model-ema --model-ema-decay 0.99996 --warmup-epochs 5 --opt-eps 1e-8 --lr 1e-3 --weight-decay .05 --drop 0 --drop-path .1 --input_size 224 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone mobilenetv3_large_100 --batch_size 64 --sched step --decay-epochs 2.4 --decay-rate .973 --opt-eps .001 --warmup-lr 1e-6 --weight-decay 1e-5 --drop 0.2 --drop-connect 0.2 --model-ema --model-ema-decay 0.9999 --lr .064 --lr-noise 0.42 0.9 --opt RMSpropTF --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone dla102x2 --weight-decay 1e-4 --lr 0.1 --input_size 224 --opt sgd --weight-decay 1e-4
python src/create_all_configs.py --user_config config_user.yaml --backbone selecsls60b --batch_size 64 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone legacy_senet154 --batch_size 64 --lr 0.6 --momentum 0.9 --weight-decay 1e-5 --opt SGD --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone ese_vovnet39b --batch_size 64 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone fbnetv3_g --batch_size 64 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone inception_v4 --batch_size 64 --lr 0.045 --lr-cycle-decay 0.94 --momentum 0.9 --opt RMSProp  --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone xception --batch_size 64 --lr 0.1 --warmup-epochs 5 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone gluon_inception_v3 --batch_size 64 --lr 0.4 --warmup-epochs 5 --save_freq 20
python src/create_all_configs.py --user_config config_user.yaml --backbone ig_resnext101_32x8d --batch_size 64 --lr 0.1 --momentum 0.9 --weight-decay 1e-4 --sched step --opt SGD --save_freq 20


