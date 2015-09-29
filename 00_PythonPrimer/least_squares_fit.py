# Lab 0
# Linear Least Squares Fit
# Author Caspar Lant

import numpy as np
import matplotlib.pyplot as plt

# load csv file
DATA = "SampleData-1.csv";
measurement, temperature, pressure, uncertainty, error = np.loadtxt(DATA, skiprows=5, unpack=True, delimiter=',');

# plot temperature vs. pressure + error bars
plt.xlabel("Temperature ($^\circ$C)");
plt.ylabel("Pressure (lb/in$ ^2$)");
plt.errorbar(temperature, pressure, error, linestyle = 'None', marker='o', mfc='orange', mec='r', ms=14, mew=1, ecolor = "k");

# linear least squares fit line
def least_squares_fit (x, y):
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    intercept = y.mean()-slope*xavg
    return slope, intercept

slope, intercept = least_squares_fit(temperature, pressure);

# create arrays to plot
y1 = slope *  150 + intercept;  # y1 = m(x1) + b
y2 = slope * -250 + intercept;  # y2 = m(x2) + b
x_range = [-250, 150];          # array of x values
y_range = [y2  , y1 ];          # array of y values

# show the graph
plt.plot(x_range,y_range);
plt.show();
