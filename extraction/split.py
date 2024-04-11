import os
import shutil

source_folder = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/img_align_celeba'
destination_test_folder = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/test'
destination_train_folder = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/train'
destination_val_folder = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/new_splits/val'
image_test_file = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/splits/celeba_test.txt'
image_train_file = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/splits/celeba_train.txt'
image_val_file = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/splits/celeba_val.txt'

def pad_filename(filename):
    # Extract the file extension
    parts = filename.split('.')
    extension = parts[-1]
    filename_without_extension = '.'.join(parts[:-1])

    # Pad the filename
    padded_filename = filename_without_extension.zfill(6) + '.' + extension
    return padded_filename

def move_file(filename, src_dir, dest_dir):

    # Check if the file exists in the source directory
    src_file = os.path.join(src_dir, filename)
    if not os.path.exists(src_file):
        print(f"File '{filename}' does not exist in the source directory '{src_dir}'.")
        return
    
    # Move the file to the destination directory
    dest_file = os.path.join(dest_dir, filename)
    shutil.move(src_file, dest_file)
    print(f"File '{filename}' moved successfully from '{src_dir}' to '{dest_dir}'.")

def extract_images(image_list_file, source_folder, destination_folder):
    # Open the text file in read mode
    with open(image_list_file, 'r') as file:
        for line in file:
            filename = line.strip()+'.jpg'
            padded_filename = pad_filename(filename)
            move_file(padded_filename, source_folder, destination_folder)

extract_images(image_test_file, source_folder, destination_test_folder)
extract_images(image_train_file, source_folder, destination_train_folder)
extract_images(image_val_file, source_folder, destination_val_folder)