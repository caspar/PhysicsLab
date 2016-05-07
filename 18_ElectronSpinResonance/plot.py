# Lab 0
# Linear Least Squares Fit
# Author Caspar Lant

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# load csv file
DATA = "data.csv";
frequency, current, twicecurrent, field = np.loadtxt(DATA, skiprows=1 , unpack=True, delimiter=',');


def least_squares_fit (x, y):
    xavg = x.mean()
    slope = ( y * ( x - xavg)).sum() / (x*(x-xavg)).sum()
    intercept = y.mean()-slope*xavg
    return slope, intercept

slope, intercept = least_squares_fit(field, frequency);

y1 = slope *  10  + intercept;  # y1 = m(x1) + b
y2 = slope *  2   + intercept;   # y2 = m(x2) + b
x_range = [2, 10];             # array of x values
y_range = [y2, y1];             # array of y values

# plot temperature vs. pressure + error bars
plt.xlabel("Magnetic Field Strength (mT)");
plt.ylabel("Resonant Frequency (MHz)");
plt.title("Resonant Frequency vs. Magnetic Field Strength");
plt.errorbar(field, frequency, yerr=2, ecolor='red', c='red',marker='.', linestyle='');
plt.plot(x_range, y_range, '-', color="blue");
plt.show()
print(slope)
# # linear least squares fit line
# def least_squares_fit (x, y):
#     xavg = x.mean()
#     slope = ( y * ( x - xavg)).sum() / (x*(x-xavg)).sum()
#     intercept = y.mean()-slope*xavg
#     return slope, intercept
#
# slope, intercept = least_squares_fit(voltage, deflection);
#
# # create arrays to plot
# y1 = slope *  15 + intercept;  # y1 = m(x1) + b
# y2 = slope *  0   + intercept;   # y2 = m(x2) + b
# x_range = [-15, 15];             # array of x values
# y_range = [y2, y1];             # array of y values
#
# print("slope: %d intercept: %d", slope, intercept)
#
# # show the graph
# # plt.plot(x_range, y_range, color="blue");
# plt.show();
