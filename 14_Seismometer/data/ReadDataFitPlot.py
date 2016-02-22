# -*- coding: utf-8 -*-
# Reads in data from data file, plots it and compares it to
# an exponentially decaying sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILENAME = "blow5.txt"
TIMESTAMP = datetime.now().strftime('%H:%M:%S')
OUTPUT = ''+ os.path.splitext(FILENAME)[0] + '_' + TIMESTAMP + '.png'
print OUTPUT

# Function defining exponentially decaying sinusoidal
def thetaU(t, A, w0, Q, phi):
    wu = w0 * np.sqrt(1.0-1.0/(4.0*Q*Q))
    return A * np.exp(-0.5*w0*t/Q) * np.sin(wu*t + phi)
# User sets these parameters to best match the data
A = 0.25
T = 14.25
Q = 9
# Amplitude
# Period (w0 = 2 pi / T)
# Q = quality factor (determines damping)
phase = 40                 # phase in degrees
# Convert phase in degrees to phase in radius for use in function
phi = np.pi * phase / 180.0     # phase in radians
time, theta = np.loadtxt(FILENAME, skiprows=130 , unpack = True)
fit = thetaU(time, A, 2.0*np.pi/T, Q, phi)
plt.plot(time, fit)
plt.axhline(color="gray")
plt.plot(time, theta)
plt.show()

fig = plt.figure()
fig.savefig(OUTPUT)
# format='png',
        # transparent=True, bbox_inches=None, pad_inches=0.1,
        # frameon=None)
