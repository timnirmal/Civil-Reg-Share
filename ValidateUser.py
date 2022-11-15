import os
import cv2
import getpass

# DATA_PATH = "Data"
# # DATASET_PATH = DATA_PATH + "/Real/"
# DATASET_PATH = DATA_PATH + "/SelectedData/"
# TESTDATA_PATH = DATA_PATH + "/Altered/SelectedData/"


database = {"umar_1": "sesamedisk", "abel_2": "nihaocloud"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for key in database.keys():
    if username == key:
        while password != database.get(key):
            password = getpass.getpass("Re-enter Your Password : ")
        break
print("User Verified")

sample = cv2.imread("./Data/Altered/Altered-Hard/2__F_Left_index_finger_CR.BMP")



