# Lab 0
# Linear Least Squares Fit
# Author Caspar Lant

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# load csv file
DATA = "planck.csv";
frequency, voltage = np.loadtxt(DATA, skiprows=1 , unpack=True, delimiter=',');

# plot temperature vs. pressure + error bars
plt.ylabel("Voltage (V)");
plt.xlabel("Frequency ($10^{14}$ Hz)");
plt.title("Voltage vs. Frequency");
plt.errorbar(frequency, voltage, yerr=0.1, linestyle = '', mec='r', ms=5    );

dv = 0.1

# linear least squares fit line
def least_squares_fit (x, y):
    xavg = x.mean()
    slope = ( y * ( x - xavg)).sum() / (x*(x-xavg)).sum()
    intercept = y.mean()-slope*xavg
    return slope, intercept

slope, intercept = least_squares_fit(frequency, voltage);

# create arrays to plot
y1 = slope *  7   + intercept;  # y1 = m(x1) + b
y2 = slope *  0   + intercept;   # y2 = m(x2) + b
x_range = [0, 7];             # array of x values
y_range = [y2, y1];             # array of y values

PLANCK = slope* 1.60217662
print("plancks constant:", PLANCK)
print("or", 1/PLANCK)
# show the graph
plt.plot(x_range, y_range, color="blue", linestyle = '-', label="Actual");

slope = 0.413566766

y1 = slope *  7 + intercept;  # y1 = m(x1) + b
y2 = slope *  0 + intercept;   # y2 = m(x2) + b
x_range = [0, 7];             # array of x values
y_range = [y2, y1];             # array of y values
PLANCK = slope * 1.60217662
# print("plancks constant:", PLANCK)
# print("or", 1/PLANCK)
# show the graph
plt.plot(x_range, y_range, color="grey",linestyle = ':', label="Expected");
plt.legend(loc='best')
plt.annotate("Slope = $6.14 * 10^{-34}$", xy=(2.27, -0.32), xytext=(2.5, -.7), arrowprops=dict(arrowstyle="->"))
# plt.legend(["slope = 1"])

plt.show();
