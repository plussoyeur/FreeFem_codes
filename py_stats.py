import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.loadtxt("stats.dat",skiprows=1)

def column(matrix,i):
    return [row[i] for row in matrix]

x = column(data,0)
R = column(data,1)
Ecc = column(data,2)
sharpness = column(data,3)

xmax = max(x)
N = 10

bin_meansR, bin_edgesR, binnumberR = stats.binned_statistic(x,R,statistic='mean',bins=10)

bin_meansEcc, bin_edgesEcc, binnumberEcc = stats.binned_statistic(x,Ecc,statistic='mean',bins=10)

bin_meansS, bin_edgesS, binnumberS = stats.binned_statistic(x,sharpness,statistic='mean',bins=10)



plt.figure(1)
plt.plot(x,R,'b.')
plt.hlines(bin_meansR,bin_edgesR[:-1],bin_edgesR[1:],colors='g',lw=5)
plt.title("Ampl vs distance from center")
plt.xlabel("Distance from center")
plt.ylabel("Amplitude")

plt.figure(2)
plt.plot(x,Ecc,'b.')
plt.hlines(bin_meansEcc,bin_edgesEcc[:-1],bin_edgesEcc[1:],colors='g',lw=5)
plt.title("Eccentricity vs distance from center")
plt.xlabel("Distance from center")
plt.ylabel("Eccentricity")


plt.figure(3)
plt.plot(x,sharpness,'b.')
plt.hlines(bin_meansS,bin_edgesS[:-1],bin_edgesS[1:],colors='g',lw=5)
plt.title("Sharpness vs distance from center")
plt.xlabel("Distance from center")
plt.ylabel("Sharpness")

plt.show()
