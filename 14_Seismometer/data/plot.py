# -*- coding: utf-8 -*-
# Reads in data from data file, plots it and compares it to
# an exponentially decaying sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILENAME = "vib2.txt"
TIMESTAMP = datetime.now().strftime('%D-%H:%M:%S')
OUTPUT = ''+ os.path.splitext(FILENAME)[0] + '_' + TIMESTAMP + '.png'
print OUTPUT

time, theta = np.loadtxt(FILENAME, skiprows=130 , unpack = True)
plt.axhline(color="gray")
plt.plot(time, theta)
plt.show()

fig = plt.figure()
fig.savefig(OUTPUT)
# format='png',
        # transparent=True, bbox_inches=None, pad_inches=0.1,
        # frameon=None)
