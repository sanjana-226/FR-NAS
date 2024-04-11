#!/bin/bash

echo "Current working directory: $(pwd)"
# Change directory to the root of your project
cd /Users/sanjanapadavala/Desktop/4-2/FR-NAS

# Activate virtual environment if needed
# . /fr/bin/activate

# Add the project root directory to the Python path
export PYTHONPATH="$PWD:$PYTHONPATH"

for f in celeba_configs/configs_default/**/*.yaml; do
  python src/train/fairness_train_celeba.py --config_path $f
done 