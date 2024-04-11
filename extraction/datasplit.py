import os
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image

celeba = r'/Users/sanjanapadavala/Desktop/4-2/FR-NAS/celeba'
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
            # Extract the class label from the filename or directory structure
            label = filename.split('_')[0]
            y.append(label)
            
    return np.array(X), np.array(y)

def split_dataset_and_save(X, y, output_dir, test_size=0.2, random_state=222):
    """
    Split a dataset into training, testing, and validation sets and save them as numpy arrays and images.
    
    Parameters:
        X : array-like, shape (n_samples, n_features)
            The input data.
        y : array-like, shape (n_samples,)
            The target labels.
        output_dir : str
            The directory to save the splits.
        test_size : float, optional (default=0.2)
            The proportion of the dataset to include in the test split.
        random_state : int, RandomState instance or None, optional (default=None)
            Controls the randomness of the training, testing, and validation splits.
    
    Returns:
        None
    """
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    val_dir = os.path.join(output_dir, 'val')
    for directory in [train_dir, test_dir, val_dir]:
        os.makedirs(directory, exist_ok=True)
    
    # Split the dataset into training and temporary testing sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Calculate the remaining portion for the validation set
    remaining_size = (1 - test_size)
    
    # Split the temporary testing set into testing and validation sets
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=random_state)
    
    # Save the splits as numpy arrays in their respective directories
    # np.save(os.path.join(train_dir, 'X_train.npy'), X_train)
    # np.save(os.path.join(train_dir, 'y_train.npy'), y_train)
    # np.save(os.path.join(test_dir, 'X_test.npy'), X_test)
    # np.save(os.path.join(test_dir, 'y_test.npy'), y_test)
    # np.save(os.path.join(val_dir, 'X_val.npy'), X_val)
    # np.save(os.path.join(val_dir, 'y_val.npy'), y_val)
    
    # Save images directly to the specified directories
    save_images(X_train, y_train, train_dir)
    save_images(X_test, y_test, test_dir)
    save_images(X_val, y_val, val_dir)

def save_images(X, y, output_dir):
    """
    Save images to the specified directory, organized by class labels.
    
    Parameters:
        X : array-like, shape (n_samples, n_features)
            The input image data.
        y : array-like, shape (n_samples,)
            The target labels.
        output_dir : str
            The directory to save the images.
    
    Returns:
        None
    """
    for image_path, label in zip(X, y):
        # Create a subdirectory for each class label
        # class_dir = os.path.join(output_dir, str(label))
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract image filename
        image_filename = os.path.basename(image_path)
        output_filename = os.path.join(output_dir, image_filename)
        
        # Open and save the image
        image = Image.open(image_path)
        image.save(output_filename)

# Load data from the folder
X, y = load_data_from_folder(input_folder)

# Split dataset and save numpy arrays and images
split_dataset_and_save(X, y, output_dir)



