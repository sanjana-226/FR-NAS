<br/>
<p align="center"><img src="img/FR-NAS.png" width=350 /></p>

----
![Crates.io](https://img.shields.io/crates/l/Ap?color=orange)
# Rethinking Bias Mitigation: Fairer Architectures Make for Fairer Face Recognition [[arxiv]](https://arxiv.org/)
<p align="center"><img src="img/fr-nas-overview.png" width=700/></p>

# Table of contents
- [Setup](#setup)
- [Download datasets](#download)
- [Download raw data files](#download_raw)
- [Create Configs](#create_configs)
- [Taining and evaluation](#train&eval)
- [Joint NAS+HPO](#jointnashpo)
    - [Search](#search)
    - [Training](#training)
    - [Evaluation](#evaluation)
    - [Analysis](#analysis2)
# Setup <a name="setup"></a>
To setup your environment use the commands below:
```
git clone https://github.com/dooleys/FR-NAS/
cd FR-NAS
conda create --name frnas python=3.9.11
conda activate frnas
pip install -r requirements.txt
```

# Download datasets <a name="download"></a>
## Create configs <a name="create_configs"></a>
| Dataset  |     Download link     | Split  | 
|----------|:-------------:|:-------------:|
| [CelebA](https://arxiv.org/pdf/1411.7766.pdf) | [download](https://drive.google.com/drive/folders/0B7EVK8r0v71pWEZsZE9oNnFzTm8?resourcekey=0-5BR16BdXnb8hVj6CNHKzLg) | Train-Val-Test |
| [RFW](https://arxiv.org/pdf/1812.00194.pdf) | [download](http://www.whdeng.cn/RFW/index.html)| Test |
| [VGGFace2](https://arxiv.org/pdf/1710.08092.pdf) | [train](https://drive.google.com/file/d/1jdZw6ZmB7JRK6RS6QP3YEr2sufJ5ibtO/view)-[test](https://www.kaggle.com/datasets/greatgamedota/vggface2-test?resource=download)  | Train-Test |
| [AgeDB](https://ibug.doc.ic.ac.uk/media/uploads/documents/agedb.pdf) | [download](https://www.dropbox.com/s/mkjsyqytd5lcai9/AgeDB.zip?dl=0) | Test |
| [LFW](http://vis-www.cs.umass.edu/lfw/) | [download](https://github.com/ZhaoJ9014/face.evoLVe#Data-Zoo) | Test |
| [CFP_FF](http://cfpw.io/paper.pdf) | [download](https://github.com/ZhaoJ9014/face.evoLVe#Data-Zoo) | Test |
| [CFP_FP](http://cfpw.io/paper.pdf) | [download](https://github.com/ZhaoJ9014/face.evoLVe#Data-Zoo) | Test |
| [CALFW](http://whdeng.cn/CALFW/?reload=true) | [download](https://github.com/ZhaoJ9014/face.evoLVe#Data-Zoo) | Test |
| [CPLPW](http://whdeng.cn/CPLFW/index.html?reload=true) | [download](https://github.com/ZhaoJ9014/face.evoLVe#Data-Zoo) | Test | 

# Large-scale study of fairness of architectures <a name="archs"></a>
The set of experiments below are for the large-scale analysis we conduct for architectures and their biases. This study is a driving force to motivate the use of NAS and HPO in the next experiments. 
## Modify user configs <a name="user_configs"></a>

After downloading the datasets above change the dataset and metadata paths in ```user_configs/config_user_celeba.yaml``` and ```user_configs/config_user_vgg.yaml``` to their respective locations. If you want to use comet for logging make sure you set the appropriate username and api key in these config files. 

## Create configs <a name="create_configs"></a>


```
bash scripts/create_configs_celeba.sh
bash scripts/create_configs_vgg.sh
```


## Train and evaluate architectures <a name="train&eval"></a> 
### CelebA
 ```
bash scripts/experiments_default_celeba.sh
bash scripts/experiments_multi_celeba.sh
```
### VGGFace2
 ```
bash scripts/experiments_default_vgg.sh
bash scripts/experiments_multi_vgg.sh
```

## Analysis <a name="analysis1"></a>
# Joint NAS+HPO <a name="jointnashpo"></a>
After the large-scale analysis we design a search space inspired by the Dual-Path-Network (DPN) and perform joint NAS and HPO using bayesian optimization in the [SMAC](https://github.com/automl/SMAC3) framework.  

Before running the search make sure to change the dataset paths and the user configs in ```search_configs/config_celeba.yaml``` and ```search_configs/config_vggface.yaml```. Then follow the following steps sequentially
## Search <a name="search"></a>
### Launch the scheduler
 ```
sbatch scripts/scheduler_dpn.sh
```
### Initialize the workers
Note: Launch the workers after the scheduler has started. Launch as many workers as you want by submitting the script below multiple times. 
 ```
sbatch scripts/workers_dpn.sh
```

### Start the distributed search
Note: You need to start schedulers and workers separately for search on CelebA and VGGFace2
 ```
sbatch scripts/job_celeba.sh
sbatch scripts/job_vgg.sh
```

## Training<a name="training"></a>
Train architectures discovered on CelebA
```
python src/search/train_smac_arch_celeba.py --seed 111 --config config1
python src/search/train_smac_arch_celeba.py --seed 111 --config config2
```

Train architecture discovered on VGGFace2
```
python src/search/train_smac_arch_vgg.py --seed 111 
```
## Analysis <a name="analysis2"></a>
# Evaluation<a name="evaluation"></a>
# Baselines <a name="baselines"></a>

