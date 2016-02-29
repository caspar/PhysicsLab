# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

filename = "edit_blow5.txt"
time1, theta1 = np.loadtxt("edit_blow2_5.txt", skiprows=2 , unpack=True)
time2, theta2 = np.loadtxt(filename, skiprows=2 , unpack=True)
time3, theta3 = np.loadtxt("blow8_5.txt", skiprows=2, unpack=True)
# time, theta = np.loadtxt("blow", skiprows=250 , unpack=True)

timestamp = datetime.now().strftime('%H:%M:%S')
print timestamp

plt.axhline(color="gray")
plt.plot(time1, theta1)
plt.plot(time2+.8, theta2)
plt.plot(time3+2.0, theta3)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.annotate("2.5cm", xy=(31.45,0.127), xytext=(29.45, 0.2),arrowprops=dict(arrowstyle="->", color='green'), color='green')
plt.annotate("5cm", xy=(45.92,0.079), xytext=(45, 0.15),arrowprops=dict(arrowstyle="->", color='blue'), color='blue')
plt.annotate("8.5cm; \nOverdamped", xy=(10,0.035), xytext=(6, 0.25),arrowprops=dict(arrowstyle="->", color='red'), color='red')
plt.show()
#
# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None)

# plt.close("all")
