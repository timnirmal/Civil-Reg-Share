import os
import cv2

DATA_PATH = "Data"
DATASET_PATH = DATA_PATH + "/SelectedData/"
TESTDATA_PATH = DATA_PATH + "/Altered/SelectedData/"


def matchfingerprint(inputfilename, samplePath=None):
    if samplePath is None:
        samplePath = TESTDATA_PATH + inputfilename
    sample = cv2.imread(inputfilename)
    if sample is None:
        print("Sample image not found")
        return
    else:
        print("Sample image found")

    best_score = counter = 0
    filename = image = kp1 = kp2 = mp = None
    print("Starting...")
    print("DATASET_PATH ",DATASET_PATH)
    print("DATASET_PATH ",DATASET_PATH)
    print()
    print("INPUT FILENAME ",inputfilename)
    print("SAMPLE PATH ",samplePath)
    print()
    print("Current Directory ",os.getcwd())
    print()

    for file in os.listdir(DATASET_PATH):
        counter += 1
        fingerprint_img = cv2.imread(DATASET_PATH + file)
        sift = cv2.SIFT_create()  # Scale Invariant Feature Transform
        keypoints_1, des1 = sift.detectAndCompute(sample, None) # des1 is the descriptor of the sample image
        keypoints_2, des2 = sift.detectAndCompute(fingerprint_img, None) # des2 is the descriptor of the image in the dataset
        # descriptor is a 128-dimensional vector that describes the keypoint in a particular image
        # fast library for approx best match KNN
        matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, {}).knnMatch(des1, des2, k=2)
        # FLANN is a library for performing fast approximate nearest neighbor searches in large datasets and
        # for high dimensional features. It contains a collection of algorithms we found to work best for
        # nearest neighbor search and a system for automatically choosing the best algorithm and optimum
        # parameters depending on the dataset.

        match_points = []
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        keypoints = 0
        if len(keypoints_1) <= len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)
        if len(match_points) / keypoints * 100 > best_score:
            best_score = len(match_points) / keypoints * 100
            filename = file
            image = fingerprint_img
            kp1, kp2, mp = keypoints_1, keypoints_2, match_points

    print("Best match:  " + filename)
    print("Best score:  " + str(best_score))
    result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=2.5, fy=2.5)
    # rotate 90 degrees
    result = cv2.rotate(result, cv2.ROTATE_90_CLOCKWISE)
    # Add text Matched smaller font size
    cv2.putText(result, "Matched", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # best score to 2 decimal places
    best_score = round(best_score, 2)
    # Add text to the image with the best match color red
    cv2.putText(result, str(round(best_score, 2))+" %", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)

    # Save the result image
    cv2.imwrite("../result.jpg", result)

    return filename, best_score, result

