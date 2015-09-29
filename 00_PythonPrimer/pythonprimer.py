#Lab 0
#coding=utf-8
#Author Caspar Lant
import numpy as np;
import matplotlib.pyplot as plt;

# load csv
DATA = "SampleData-1.csv";
measurement, temperature, pressure, uncertainty, error = np.loadtxt(DATA, skiprows=5, unpack=True, delimiter=',');

# plot data
# plt.xlabel("Temperature ($^\circ$C)");
# plt.ylabel("Pressure (lb/in$ ^2$)");

# with error bars
plt.errorbar(temperature, pressure, error, linestyle = 'None', marker='d', mfc='yellow', mec='r', ms=20, mew=1, ecolor = "k");
plt.show();

#####################
# coupled pendulums #
#####################
A = 0.1
w1 = 2 * np.pi * 5
w2 = 2 * np.pi * 5.2
theta_a1 = []
theta_b1 = []
theta_a2 = []
theta_b2 = []
times = [];
for t in range (0,400):
    theta_a1.append(A * np.cos(w1 * t / 200) + A * np.cos(w2 * t / 200));
    theta_b1.append(A * np.cos(w1 * t / 200) - A * np.cos(w2 * t / 200));
    theta_a2.append(2 * A * np.cos((w2 - w1) / 2 * t / 200) * np.cos((w2 + w1) / 2 * t / 200));
    theta_b2.append(2 * A * np.sin((w2 - w1) / 2 * t / 200) * np.sin((w2 + w1) / 2 * t / 200));

    times.append(t)

plt.plot(times, theta_a1);
plt.plot(times, theta_b1);

plt.plot(times, theta_a2);
plt.plot(times, theta_b2);

plt.show();
