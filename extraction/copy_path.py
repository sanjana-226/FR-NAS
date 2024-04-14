import os
from os.path import abspath
import shutil
from tqdm.auto import tqdm

def get_img(image: int):
    path = os.path.join(abspath("../dataset/img_align_celeba"), f"{image:06d}.jpg")
    if not os.path.exists(path):
        raise Exception(f"Can't find path ${path}")
    return path


def copy_images(classes_file, target_root):
    images = open(classes_file).readlines()
    for image in tqdm(images, desc=os.path.basename(classes_file)):
        if "txt" in image:
            continue
        print(image)
        image = int(image.strip())
        image_path = get_img(image)
        new_folder = os.path.join(target_root, str(int(image)))
        #print(f"'{image_path}' -> '{new_folder}'")
        os.makedirs(new_folder, exist_ok=True)
        shutil.copy(image_path, new_folder)


copy_images(abspath("../splits/celeba_train.txt"), abspath("../new-splits2/train-splits"))
copy_images(abspath("../splits/celeba_test.txt"), abspath("../new-splits2/test"))
copy_images(abspath("../splits/celeba_val.txt"), abspath("../new-splits2/val"))

