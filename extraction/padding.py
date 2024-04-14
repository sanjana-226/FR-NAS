import os
import shutil

# train_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train'
test_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/test'
val_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/val'
male_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train-splits/male'
female_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train-splits/female'

# new_train_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/unpadded_splits/train'
new_test_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/unpadded-splits/test'
new_val_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/unpadded-splits/val'
new_male_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/unpadded-splits/train-splits/male'
new_female_path=r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/unpadded-splits/train-splits/female'

def remove_padding(old_directory, new_directory):
    # Get list of files in the directory
    files = os.listdir(old_directory)

    # Iterate over each file
    for filename in files:
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        
        # Remove leading zeros from the file name
        new_name = name.lstrip('0')

        # If the new name is different from the old one, rename the file
        if new_name != name:
            old_path = os.path.join(old_directory, filename)
            new_path = os.path.join(new_directory, new_name + ext)

            # Create a copy with the new name
            shutil.copy2(old_path, new_path)
            print(f"Created copy '{new_name + ext}' from '{filename}'")

# remove_padding(train_path)
remove_padding(test_path, new_test_path)
remove_padding(val_path, new_val_path)
remove_padding(male_path,new_male_path)
remove_padding(female_path,new_female_path)

