# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

def count_people(img_path):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # load the image and resize it to (1) reduce detection time
    # and (2) improve detection accuracy
    image = cv2.imread(img_path)
    image = imutils.resize(image, width=min(1000, image.shape[1]))
    
    # detect people in the image and return the coordinates of bounding rectangle
    (rects, weights) = hog.detectMultiScale(image, winStride=(2, 2),
        padding=(8, 8), scale=1.05)
    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    picks = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    num_people = len(picks)

    return num_people
