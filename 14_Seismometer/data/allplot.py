# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

filename = "edit_blow5.txt"
time1, theta1 = np.loadtxt("edit_blow2_5.txt", skiprows=2 , unpack=True)
time2, theta2 = np.loadtxt(filename,   skiprows=2 , unpack=True)
# time, theta = np.loadtxt("blow", skiprows=250 , unpack=True)

timestamp = datetime.now().strftime('%H:%M:%S')
print timestamp

plt.axhline(color="gray")
plt.plot(time1, theta1)
plt.plot(time2+.8, theta2)
plt.show()
#
# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None)

# plt.close("all")
