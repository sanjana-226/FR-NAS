import pandas as pd
import shutil
import os

# Source folder containing the images
source_folder = '/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train'

# Destination folders for each label
female_folder = '/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train-splits/female'
male_folder = '/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train-splits/male'
csv_file = '/Users/sanjanapadavala/Desktop/4-2/FR-NAS/extraction/class_labels.csv'

# Create destination folders if they don't exist
os.makedirs(female_folder, exist_ok=True)
os.makedirs(male_folder, exist_ok=True)

# Function to get label for an image from the CSV
def get_label(image_id):
    labels_df = pd.read_csv(csv_file)
    matching_rows = labels_df.loc[labels_df['image_id'] == image_id]
    # # print("Image ID:", image_id)
    # print("Matching rows:", matching_rows)
    if not matching_rows.empty:
        label = matching_rows.iloc[0]['Male']
        return label
    else:
        return None

count = 0
# Iterate over each image in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg'):
        count = count+1
        image_id = os.path.splitext(filename)[0]+'.jpg'
        label = get_label(image_id)

        # Construct source and destination paths for the image
        source_path = os.path.join(source_folder, filename)
        
        if label == -1:
            destination_path = os.path.join(female_folder, filename)
        elif label == 1:
            destination_path = os.path.join(male_folder, filename)
        else:
            continue
        
        # Move the image to the appropriate destination folder
        shutil.move(source_path, destination_path)
        if count%100==0:
            print(count)

print("All images moved successfully.")
