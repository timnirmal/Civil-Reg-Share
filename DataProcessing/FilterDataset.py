import os
import shutil

#DATASET_PATH = "../Data/Real/"
DATASET_PATH = "../Data/Altered/Altered-Hard/"

# Read the image names and copy file which include "index" and "Right" in their name
for file in os.listdir(DATASET_PATH):
    if "index" in file and "Right" in file:
        shutil.copy(DATASET_PATH + file, "../Data/SelectedData/" + file)
        print(file)

