#!/usr/bin/env python3
import serial
import numpy as np
import matplotlib.pyplot as plt
import csv


def moving_avg(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1 :] / n


chunk_size = 80
num_chunks = 6

with serial.Serial("/dev/ttyACM0") as s:
    # with open("data2.txt") as s:
    data = []
    while True:
        for _ in range(chunk_size):
            data += [int(s.readline())]
        dataToShow = data[-(chunk_size * num_chunks) :]

        ax1 = plt.subplot(2, 1, 1)
        ax2 = plt.subplot(2, 1, 2)

        plt.sca(ax1)  # Set current axes
        # plt.plot(moving_avg(dataToShow, 20))
        plt.plot(dataToShow)
        # plt.xlim(0, 3)
        # plt.ylim(0, 400000)

        """
          plt.sca(ax2)  # Set current axes

          smoothed = moving_average(np.diff(dataToShow), 1500)
          plt.plot(smoothed)
          """

        plt.pause(0.0001)
        plt.clf()

# plt.show()
