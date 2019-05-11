#!/usr/bin/env python3
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.interpolate as interp

fs = float(sys.argv[2])  # FPS
interp_num = 10

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


xs = np.array(xs) - np.mean(xs)  # Remove DC offset

spl = interp.UnivariateSpline(ts, xs)
ts = np.linspace(ts[0], ts[-1], len(ts) * interp_num)
xs = spl(ts)
fs *= interp_num

four = np.fft.rfft(xs)
freqs = np.fft.rfftfreq(len(xs), 1 / fs)
# plt.plot(freqs, four)
# plt.show()


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

filt = sig.butter(5, (5 / fs), analog=False)
ys_f = sig.lfilter(filt[0], filt[1], ys)


def adj(xs):
    return (np.array(xs) - np.mean(xs)) / np.var(xs)


def plot(xs):
    plt.plot(ts, adj(xs))


plot(xs)
# plot(carrier)
plot(ys)
plot(ys_f)
plt.show()
