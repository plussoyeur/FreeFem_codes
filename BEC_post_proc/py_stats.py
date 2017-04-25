import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("statsnohessian.dat",skiprows=1)
#data = np.loadtxt("statsabrikosov.dat",skiprows=1)

def column(matrix,i):
    return [row[i] for row in matrix]

distfromcenter = column(data,0)
vortexcoreradius = column(data,1)


fig = plt.figure(figsize=(6,4),dpi=80)
plt.plot(distfromcenter,vortexcoreradius,'b.')
plt.xlabel("Normalised Distance from center: " r'$\frac{r}{R_{BEC}}$')
plt.ylabel("Vortex core radius" r' $r_v$ ')

fig.savefig("vortexradius_vs_distance.png")
plt.show()
