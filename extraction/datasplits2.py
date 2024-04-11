import os
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image

input_folder = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/dataset/img_align_celeba'
output_dir = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/dataset/splits'

def load_data_from_folder(input_folder):
    """
    Load data from a folder where each file corresponds to a sample.
    
    Parameters:
        input_folder : str
            The path to the input folder.
    
    Returns:
        X : array-like, shape (n_samples, n_features)
            The input data.
        y : array-like, shape (n_samples,)
            The target labels.
    """
    X = []
    y = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            # Add image filename to the list
            X.append(os.path.join(input_folder, filename))
            # Assuming the label is encoded in the filename or directory structure
            label = filename.split('_')[0]  
            y.append(label)
            
    return np.array(X), np.array(y)

def batch_save_images(X, y, output_dir, batch_size=50, limit=50):
    """
    Batch save images to the specified directory, limiting the number of images processed for each label.
    
    Parameters:
        X : array-like, shape (n_samples, n_features)
            The input image data.
        y : array-like, shape (n_samples,)
            The target labels.
        output_dir : str
            The directory to save the images.
        batch_size : int, optional (default=50)
            The size of each batch.
        limit : int, optional (default=50)
            The maximum number of images to process for each label.
    
    Returns:
        None
    """
    print("Starting batch image saving process...")
    num_samples = len(X)
    num_batches = (num_samples + batch_size - 1) // batch_size  # Calculate the number of batches
    
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, num_samples)
        batch_X = X[start_idx:end_idx]
        batch_y = y[start_idx:end_idx]
        save_images(batch_X, batch_y, output_dir, limit)
    
    print("Batch image saving process completed.")

def save_images(X, y, output_dir, limit=50):
    """
    Save images to the specified directory, limiting the number of images processed for each label.
    
    Parameters:
        X : array-like, shape (n_samples, n_features)
            The input image data.
        y : array-like, shape (n_samples,)
            The target labels.
        output_dir : str
            The directory to save the images.
        limit : int, optional (default=50)
            The maximum number of images to process for each label.
    
    Returns:
        None
    """
    print("Starting image saving process...")
    processed_images = 0
    for image_path, label in zip(X, y):
        if processed_images >= limit:
            break  # Stop processing images for this label if the limit is reached
        # Assuming X contains file paths
        print(f"Processing image: {image_path}, Label: {label}")
        try:
            image_filename = os.path.basename(image_path)
            output_filename = os.path.join(output_dir, f"{label}_{image_filename}")
            image = Image.open(image_path)
            image.save(output_filename)
            processed_images += 1
        except Exception as e:
            print(f"Error occurred while processing image: {image_path}")
            print(f"Error details: {str(e)}")
    print("Image saving process completed.")

# Load data from the folder
X, y = load_data_from_folder(input_folder)

# Batch save images
batch_save_images(X, y, output_dir)

