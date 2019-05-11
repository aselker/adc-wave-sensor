#!/usr/bin/env python3
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import sys


class LaserViewer:
    def __init__(self, stream):
        self.xs = []
        self.ys = []
        self.ts = []
        self.max_len = 100
        self.cap = cv2.VideoCapture(stream)
        self.cap.set(cv2.CAP_PROP_FPS, 120)
        style.use("fivethirtyeight")

        fig = plt.figure()
        self.ax1 = fig.add_subplot(2, 1, 1)
        self.ax2 = fig.add_subplot(2, 1, 2)

        self.ani = animation.FuncAnimation(fig, self.animate, interval=10)

        plt.show()

    def animate(self, i):

        # Capture frame-by-frame
        ret, frame = self.cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 0, 254])
        upper_red = np.array([180, 30, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        im2, contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) != 0:
            # draw in blue the contours that were founded
            cv2.drawContours(frame, contours, -1, 255, 3)

            # find the biggest area
            c = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(c)
            self.xs.append(x)
            self.ys.append(y)
            self.ts.append(time.time())

            if len(self.xs) > self.max_len:
                self.xs = self.xs[-self.max_len :]
            if len(self.ys) > self.max_len:
                self.ys = self.ys[-self.max_len :]
            if len(self.ts) > self.max_len:
                self.ts = self.ts[-self.max_len :]
            # draw the book contour (in green)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self.ax1.clear()
            self.ax2.clear()
            self.ax1.plot(self.ts, self.ys)
            self.ax2.plot(self.ts, self.xs)

        # # show the images
        # cv2.imshow("Result", np.hstack([image, output]))
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)


lv = LaserViewer(sys.argv[1])


# When everything done, release the capture
lv.cap.release()
lv.cv2.destroyAllWindows()
