#!/usr/bin/env python3
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import sys


max_len = 100
cap = cv2.VideoCapture(sys.argv[1])

while True:
    ret, frame = cap.read()
    if not ret:
        cap.release()
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 0, 254])
    upper_red = np.array([180, 30, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    im2, contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) != 0:
        # find the biggest area
        c = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)
    else:
        x = -1
        y = -1

    print("%g, %g" % (x, y))
