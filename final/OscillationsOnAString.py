import numpy as np;
import matplotlib.pyplot as plot
import math;

data = "Amaxdata.csv";

# load csv
time, displacement, error = np.loadtxt(data, skiprows=0, unpack = True, delimiter=',');
times = [];
logs = []

for t in time:
    print time[t+1] - time[t]

for d in displacement:
    print math.log(displacement[d]);

print (time[len(time)-1] - time[0])/(len(time)-1)
# plot.plot(time, displacement);
plot.errorbar(time, displacement, error);
# plot.plot(time, logs);
plot.show();
