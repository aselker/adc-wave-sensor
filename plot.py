#!/usr/bin/env python3
import matplotlib.pyplot as plt

data = []
with open("data.txt") as f:
    data = [int(l) for l in f]

plt.plot(data, ".")
plt.show()
