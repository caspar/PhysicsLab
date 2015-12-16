import numpy as np;
import matplotlib.pyplot as plot
import math;
from scipy.optimize import curve_fit

#http://www.physics.nyu.edu/pine/pymanual/html/chap8/chap8_fitting.html

data = "Amaxdata.csv";

# load csv
t_max, A_max, A_error = np.loadtxt(data, skiprows=0, unpack = True, delimiter=',');
# plot.errorbar(t_max, A_max, A_error);

times = [];
# logs = np.array(logs, dtype=float);

def exp(x,a,b,c):
    return a * np.exp(-b * x) + c;

def gamma(A, t):
    # ln(A_max(t_max)) = ln(A_0) - .5 * gamma * t_max => gamma =
    gamma = (math.log(A_max[0]) - math.log(A))*2/t
    print gamma
    return gamma

gamma = np.array(A_max, dtype=float);

# for t in t_max:
#     print t_max[t+1] - t_max[t]

# for d in A_max:
#     logs[d] = math.log(A_max[d]);

# print (t_max[len(t_max)-1] - t_max[0])/(len(t_max)-1)
# plot.plot(t_max, A_max);
# plot.plot(t_max, np.polyfit(A_max));
for i in t_max:
    plot.plot(t_max[i], gamma(A_max[i], t_max[i]))
# plot.plot(t_max, logs);
plot.show();
