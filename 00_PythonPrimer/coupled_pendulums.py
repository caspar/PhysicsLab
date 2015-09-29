# Lab 0
# Coupled Pendulums
# Author Caspar Lant
import numpy as np;
import matplotlib.pyplot as plt;

# define constants
A  = 0.1;                # amplitude
w1 = 2 * np.pi * 5;      # angular velocity
w2 = 2 * np.pi * 5.2;    # angular velocity

# instantiate data arrays
theta_a1 = [];
theta_b1 = [];
theta_a2 = [];
theta_b2 = [];
times    = [];

for t in range (0,400):
    theta_a1.append(A     * np.cos(w1 * t / 200) + A        * np.cos(w2 * t / 200));
    theta_b1.append(A     * np.cos(w1 * t / 200) - A        * np.cos(w2 * t / 200));
    theta_a2.append(2 * A * np.cos((w2 - w1) / 2 * t / 200) * np.cos((w2 + w1) / 2 * t / 200));
    theta_b2.append(2 * A * np.sin((w2 - w1) / 2 * t / 200) * np.sin((w2 + w1) / 2 * t / 200));
    times.append(t)

plt.plot(times, theta_a1);
plt.plot(times, theta_b1);

plt.plot(times, theta_a2);
plt.plot(times, theta_b2);

plt.show();
