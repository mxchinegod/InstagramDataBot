import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import os

data = []
x = []
y = []
with open(os.getcwd() + '\data.txt', 'r') as f:
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
t = np.arange(0., 1.0, 60.0)
plt.plot(y, 'r-')
plt.grid()
plt.axis([0, 2000, 4500, 6000])
plt.show()