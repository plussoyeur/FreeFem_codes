from numpy import *
from scipy import stats
import matplotlib.pyplot as plt

data = loadtxt("stats.dat")

def column(matrix,i):
    return [row[i] for row in matrix]

x = column(data,0)
R = column(data,1)
Ecc = column(data,2)
sharpness = column(data,3)


bin_means, bin_edges, binnumber = stats.binned_statistic(x,sharpness,statistic='mean',bins=[0,2,4,6,8,10,12])

plt.plot(x,sharpness,'b.')
plt.hlines(bin_means,bin_edges[:-1],bin_edges[1:],colors='g',lw=5)
plt.title("Ampl vs distance from center")
plt.show()