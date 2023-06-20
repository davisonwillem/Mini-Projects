import numpy as np
import matplotlib.pyplot as plt
N = int(input("Gis a number of points:"))
xs = np.array([np.random.random(N)])
ys = np.array([np.random.random(N)])
inc=0
i=0
while i < N:
    d=(np.sqrt(xs[0,i]*xs[0,i]+ys[0,i]*ys[0,i]))
    if d < 1:
        inc=inc+1
    i=i+1
print ((inc/N)*4)