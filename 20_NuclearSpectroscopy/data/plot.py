# -*- coding: utf-8 -*-
# Reads in data from data file, plots it and compares it to
# an exponentially decaying sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Lead 1.1 9,246
#
# Lead 2.4 7,862
#
# Lead 3.4 6,849
#
# Lead 8.4 4980
#
# 0 10,338

counts = np.array([10338, 9246, 7862, 6849, 4980])
thickness = np.array([0, 1.1, 2.4, 3.4, 8.4])
thicknesserror = np.array([0.1,0.1,0.1,0.1,0.1])

def least_squares_fit (x, y):
    xavg = x.mean()
    slope = ( y * ( x - xavg)).sum() / (x*(x-xavg)).sum()
    intercept = y.mean()-slope*xavg
    return slope, intercept

slope, intercept = least_squares_fit(thickness, np.log(counts));

y1 = slope *  10  + intercept;  # y1 = m(x1) + b
y2 = slope *  0   + intercept;   # y2 = m(x2) + b
x_range = [0, 10];             # array of x values
y_range = [y2, y1];             # array of y values

plt.xlabel("Lead Thickness (mm)")
plt.ylabel(r'ln(Counts) ($\beta$)')
plt.title('Beta Particles Detected vs. Shield Thickness')

plt.errorbar(thickness, np.log(counts), xerr=0.3, yerr=0.000007*counts, ecolor='red', c='red',marker='.', linestyle='' )
plt.plot(x_range, y_range, '-', color="blue");
plt.text(1,8.4, r' Absorption Coefficient: 0.086 $\beta / {\rm mm}$')
print(slope, intercept)
plt.axis([0, 10, None, None])
plt.show()
