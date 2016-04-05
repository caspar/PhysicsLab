import math
import numpy as np
import matplotlib.pyplot as plt

# constants
h    = 6.62607004e-34
hbar = h/(2*math.pi)
k_B  = 1.38064852e-23
T    = 293 # room temperature
c    = 299792458

# range of values
wavelength = np.arange(0, 5e-5, 1e-7)

# spectral radiance
S = (8*math.pi*hbar*c /(wavelength**5)) / (math.e**(h*c/(wavelength*k_B*T))-1)

# label axes
plt.title("Radiance of a Blackbody")
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral Radiance (W/sr)")

plt.plot(wavelength, S)
plt.show()
