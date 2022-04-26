python create_phase1b_configs.py --user_config config_user.yaml --backbone cait_xs24_384 --drop-path 0.1 --model-ema -model-ema-decay 0.99996 --opt adamw --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --decay-epochs 30 --warmup-epochs 5 --warmup-lr 1e-6 --min-lr 1e-5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone cait_s24_224 --drop-path 0.1 --model-ema -model-ema-decay 0.99996 --opt adamw --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --decay-epochs 30 --warmup-epochs 5 --warmup-lr 1e-6 --min-lr 1e-5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone coat_lite_small --drop-path 0.0  --model-ema -model-ema-decay 0.99996  --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30 --warmup-epochs 5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone convit_base --model-ema --model-ema-decay 0.99996  --drop-path 0.1 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30 --min-lr 1e-5  --warmup-epochs 5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone twins_svt_base --model-ema --model-ema-decay 0.99996  --drop-path 0.1 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30  --min-lr 1e-5  --warmup-epochs 5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone twins_svt_base --model-ema --model-ema-decay 0.99996  --drop-path 0.1 --weight-decay 0.05 --lr 5e-4 --warmup-lr 1e-6 --min-lr 1e-5 --decay-epochs 30  --min-lr 1e-5  --warmup-epochs 5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone swin_base_patch4_window7_224 --drop-path 0.5 --model-ema --decay-epochs 30 --warmup-epochs 5 --weight-decay 1e-8 --lr 2e-05 --warmup-lr 2e-08 --min-lr 2e-07 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone dla102x2 --weight-decay 1e-4 --lr 0.1 --opt sgd --weight-decay 1e-4
python create_phase1b_configs.py --user_config config_user.yaml --backbone cspdarknet53 --lr 1e-4 --opt adam  --weight-decay 0.0005
python create_phase1b_configs.py --user_config config_user.yaml --backbone tf_efficientnet_b7_ns --sched step  --decay-epochs 2.4 --decay-rate .97 --opt rmsproptf --opt-eps .001 --warmup-lr 1e-6 --weight-decay 1e-5 --drop 0.3 --drop-connect 0.2 --model-ema --model-ema-decay 0.9999  --lr .016
python create_phase1b_configs.py --user_config config_user.yaml --backbone tf_efficientnet_l2_ns --sched step  --decay-epochs 2.4 --decay-rate .97 --opt rmsproptf --opt-eps .001 --warmup-lr 1e-6 --weight-decay 1e-5 --drop 0.3 --drop-connect 0.2 --model-ema --model-ema-decay 0.9999  --lr .016
python create_phase1b_configs.py --user_config config_user.yaml --backbone ghostnet_100 --lr 0.1 --momentum 0.9 --weight-decay 0.0001 --opt sgd --sched multistep
python create_phase1b_configs.py --user_config config_user.yaml --backbone hrnet_w64 --opt sgd --lr 0.05 --weight-decay 0.0001
python create_phase1b_configs.py --user_config config_user.yaml --backbone dpn107 --sched multistep --lr 0.001 --weight-decay 0.0001 --opt sgd
python create_phase1b_configs.py --user_config config_user.yaml --backbone densenet161 --lr 0.1 --weight-decay 0.0001 --drop 0.2 --sched multistep --opt sgd
python create_phase1b_configs.py --user_config config_user.yaml --backbone convnext_large_384_in22ft1k --drop-path 0.1 --lr 4e-3 --model-ema --opt adamw --opt_eps 1e-8 --weight_decay 0.05 --min_lr 1e-6 --warmup_epochs 20
python create_phase1b_configs.py --user_config config_user.yaml --backbone dm_nfnet_f4 --model-ema --opt sgd_agc --weight-decay 2e-5 --opt-eps 1e-3 --sched WarmupCosineDecay --lr 0.1 # need to modify code to support sgd_agc and warup_cosine decay from here https://github.com/deepmind/deepmind-research/blob/master/nfnets/optim.py
python create_phase1b_configs.py --user_config config_user.yaml --backbone xcit_large_24_p8_384_dist --drop-path 0.1 --model-ema -model-ema-decay 0.99996 --opt adamw --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --decay-epochs 30 --warmup-epochs 5 --warmup-lr 1e-6 --min-lr 1e-5 --batch_size 64
python create_phase1b_configs.py --user_config config_user.yaml --backbone xcit_medium_24_p8_224_dist --drop-path 0.1 --model-ema -model-ema-decay 0.99996 --opt adamw --opt-eps 1e-8 --weight-decay 0.05 --lr 5e-4 --decay-epochs 30 --warmup-epochs 5 --warmup-lr 1e-6 --min-lr 1e-5 --batch_size 64
