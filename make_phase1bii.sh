
for f in configs/**/*.yaml; do
  echo "python python src/fairness_train_timm.py --config_path $f"
done 
