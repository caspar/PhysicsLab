import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# constants
e          = 1.6e-19
c          = 299792458
h_expected = 6.62607004e-34

# load csv file
DATA = "data.csv";
wavelength, voltage, v_uncertainty = np.loadtxt(DATA, skiprows=1 , unpack=True, delimiter=',');

frequency = c/wavelength

# plot temperature vs. pressure + error bars
plt.ylabel("Voltage (V)");
plt.xlabel("Frequency (Hz)");
plt.title("Voltage vs. Frequency");
plt.errorbar(frequency, voltage, v_uncertainty, linestyle='', color='red');

# Kent Linefit
def LineFit(x,y,err):
    err2 = err**2
    norm = (1./err2).sum()
    def hat(x):
        return (x/err2).sum()/norm
    xhat = hat(x)
    yhat = hat(y)
    diff = (x-xhat)
    b = (diff*y/err2).sum()/(diff*x/err2).sum()
    a = yhat - b*xhat
    sb = np.sqrt(1./((diff)*x/err2).sum())
    sa = np.sqrt(sb**2*(x**2/err2).sum()/norm)
    return a,b,sa,sb

slope, intercept, s_slope, s_intercept = LineFit(frequency, voltage, v_uncertainty)

# create arrays to plot
y1 = slope *  5e14   + intercept;   # y1 = m(x1) + b
y2 = slope *  7e14   + intercept;   # y2 = m(x2) + b
x_range = [5e14, 7e14];             # array of x values
y_range = [y1, y2];                 # array of y values

# show the graph
plt.plot(x_range, y_range, color="blue", linestyle = '-', label="Actual");

planck = slope * e
work   = - intercept * e

print(s_slope)
print(s_intercept)

print(planck)
print(work)
plt.show();
