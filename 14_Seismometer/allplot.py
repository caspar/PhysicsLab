# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

time, theta = np.loadtxt("blow2_5.txt", skiprows=250 , unpack=True)
time, theta = np.loadtxt("blow5.txt", skiprows=250 , unpack=True)
# time, theta = np.loadtxt("blow", skiprows=250 , unpack=True)
plt.axhline(color="gray")
plt.plot(time, theta)
plt.show()
