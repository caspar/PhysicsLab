# Lab 0
# Linear Least Squares Fit
# Author Caspar Lant

import numpy as np
import matplotlib.pyplot as plt

# load csv file
DATA = "IdealGasLaw.csv";
measurement, pressure, temperature, uncertainty, error = np.loadtxt(DATA, skiprows=5, unpack=True, delimiter=',');

# plot temperature vs. pressure + error bars
plt.xlabel("Pressure (kPa)");
plt.ylabel("Temperature (K)");
plt.title("Temperature vs. Pressure");
plt.errorbar(pressure, temperature, error, uncertainty, linestyle = ':', mec='r', ms=0, ecolor = "red");

# linear least squares fit line
def least_squares_fit (x, y):
    xavg = x.mean()
    slope = ( y * ( x - xavg)).sum() / (x*(x-xavg)).sum()
    intercept = y.mean()-slope*xavg
    return slope, intercept

slope, intercept = least_squares_fit(temperature, pressure);

# create arrays to plot
y1 = slope *  400 + intercept;  # y1 = m(x1) + b
y2 = slope *  0   + intercept;   # y2 = m(x2) + b
x_range = [0, 400];             # array of x values
y_range = [y2, y1];             # array of y values

print("slope: %d intercept: %d", slope, intercept)

# show the graph
plt.plot(y_range, x_range, color="blue");
plt.show();
