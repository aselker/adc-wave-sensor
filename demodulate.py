#!/usr/bin/env python3
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

fs = float(sys.argv[2])  # FPS

xs = []
ys = []
ts = []
t = 0
with open(sys.argv[1]) as f:
    c = csv.reader(f, delimiter=",")
    for row in c:
        xs += [int(row[0])]
        ys += [int(row[1])]
        t += 1 / fs
        ts += [t]

# Pick the channel with higher variance; then call it 'xs' cause that's a nice name
if np.var(xs) > np.var(ys):
    print("Using xs")
    del ys
else:
    print("Using ys")
    xs = ys
    del ys

four = np.fft.rfft(xs)
freqs = np.fft.rfftfreq(len(xs), 1 / fs)

# Find the carrier freq and phase by finding the peak that's not next to 0
# Find the highest point in four where freq >= 5
(cfreq, cmag) = max([x for x in zip(freqs, four) if x[0] >= 5], key=lambda x: abs(x[1]))
cmag = cmag / abs(cmag)  # Normalize magnitude
print(cfreq, cmag)

phases = np.array(ts) * cfreq * 2 * np.pi
carrier = np.real((np.cos(phases) + (1j) * np.sin(phases)) * cmag)

ys = xs * carrier

"""
plt.plot(ts, xs)
plt.plot(ts, ys)
plt.show()
plt.plot(freqs, four)
plt.plot(freqs, np.fft.rfft(ys))
plt.show()
"""

filt = sig.butter(4, (7 / fs), analog=False)
ys_f = sig.lfilter(filt[0], filt[1], ys)
plt.plot(ts, ys_f)
plt.show()
