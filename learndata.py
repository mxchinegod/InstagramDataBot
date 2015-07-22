import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import os

xaxis = int(raw_input("How long (minutes) is the data?: "))
yaxis = int(raw_input("How tall (followers) is the data?: "))
interval = int(raw_input("What was the interval (in seconds)?: "))
data = []
x = []
y = []
with open(os.path.dirname(os.path.realpath(__file__)) + '\data.txt', 'r') as f:
    for line in f:
        data.append(line.split(':'))

for i in data:
    y.append(i[0])
    x.append(i[1])
    x = ([i[0].replace('\n', '') for i[0] in x])
    x = ([i[0].replace(' ', '') for i[0] in x])
plt.title("Instagram")
plt.xlabel("One Minute Intervals")
plt.ylabel("Follower count relative to " + str(y[0]))
t = np.arange(0., 1.0, interval)
plt.plot(y, 'r-')
plt.grid()
plt.axis([0, xaxis, yaxis/2, yaxis])
plt.show()