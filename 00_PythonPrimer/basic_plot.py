# Lab 0
# Basic Plot of Temperature vs. Pressure
# Author Caspar Lant
import numpy as np;
import matplotlib.pyplot as plt;

# load csv
DATA = "SampleData-1.csv";
measurement, temperature, pressure, uncertainty, error = np.loadtxt(DATA, skiprows=5, unpack=True, delimiter=',');

# plot temperature vs. pressure + error bars
plt.xlabel("Temperature ($^\circ$C)");
plt.ylabel("Pressure (lb/in$ ^2$)");
plt.errorbar(temperature, pressure, error, linestyle = 'None', marker='o', mfc='orange', mec='r', ms=14, mew=1, ecolor = "k");
plt.show();
