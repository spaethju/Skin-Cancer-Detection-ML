import os

import shutil

dataset_local_path = "/data/scratch/einig/SkinCancerData"


prefix = '/train'
dataset_path = '../datasets/training.dataset'
# prefix = '/val'
# dataset_path = '../datasets/validation.dataset'
# prefix = '/test'
# dataset_path = '../datasets/test.dataset'

if not os.path.exists(dataset_local_path + prefix):
    os.makedirs(dataset_local_path + prefix)

if not os.path.exists(dataset_local_path + prefix + "/Images"):
    os.makedirs(dataset_local_path + prefix + "/Images")

if not os.path.exists(dataset_local_path + prefix + "/Descriptions"):
    os.makedirs(dataset_local_path + prefix + "/Descriptions")

with open(os.path.expanduser(dataset_path)) as f:
    for line in f:
        src_path = dataset_local_path + "/Images/" + line.strip() + "_resized.jpg"
        dest_path = dataset_local_path + prefix + "/Images/" + line.strip() + "_resized.jpg"

        try:
            shutil.move(src=src_path, dst=dest_path)
        except:
            print("following file was not found: {}".format(src_path) )

        src_path = dataset_local_path + "/Descriptions/" + line.strip()
        dest_path = dataset_local_path + prefix + "/Descriptions/" + line.strip()

        try:
            shutil.move(src=src_path, dst=dest_path)
        except:
            print("following file was not found: {}".format(src_path) )






