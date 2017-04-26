import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#data = np.loadtxt("statsnohessian.dat",skiprows=1)
data = np.loadtxt("statsabrikosov.dat",skiprows=1)


def column(matrix,i):
    return [row[i] for row in matrix]

x = column(data,0)
Rv = column(data,1)
#Ecc = column(data,2)
#sharpness = column(data,3)

#xmax = max(x)
#N = 10

bin_meansRv, bin_edgesRv, binnumberRv = stats.binned_statistic(x,Rv,statistic='mean',bins=10)

#bin_meansEcc, bin_edgesEcc, binnumberEcc = stats.binned_statistic(x,Ecc,statistic='mean',bins=10)

#bin_meansS, bin_edgesS, binnumberS = stats.binned_statistic(x,sharpness,statistic='mean',bins=10)



plt.figure(1)
plt.plot(x,Rv,'b.')
plt.hlines(bin_meansRv,bin_edgesRv[:-1],bin_edgesRv[1:],colors='g',lw=5)
plt.title("Vortex core radius vs distance from center")
plt.xlabel("Distance from center normalized : " r'$\frac{r}{R_{BEC}}$')
plt.ylabel("Vortex core radius")


plt.show()
