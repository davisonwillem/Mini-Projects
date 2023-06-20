import numpy as np
import matplotlib.pyplot as plt

#%%#

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def comppowers(cr,ci):
    r,theta=cart2pol(cr,ci)
    xs=np.array([cr])
    ys=np.array([ci])
    for i in range (300):
        r=r**1.01
        theta=theta*1.01
        x,y=pol2cart(r,theta)
        xs=np.append(xs,x)
        ys=np.append(ys,y)
    plt.plot(xs,ys)

plt.figure()
plt.xlim(-5,5)
plt.ylim(-4,4)
ang=np.arange(0,6.3,100)
comppowers(0,1)
comppowers(float(input("Real part: ")),float(input("Imaginary part: ")))
comppowers(float(input("Real part: ")),float(input("Imaginary part: ")))