import numpy as np
import matplotlib.pyplot as plt
from numpy import random

L = 100
particles = 100000
h = np.zeros(L)
w = np.zeros(particles)

for i in range(particles):
    number = random.randint(0,L)
    h[number] = max(h[(number-1)%L] , h[number] , h[(number+1)%L]) + 1

    w[i] = np.var(h)

t = np.linspace(0,len(w)/L , len(w))
plt.plot(t, w)
plt.xscale('log')
plt.yscale('log')
plt.show()
