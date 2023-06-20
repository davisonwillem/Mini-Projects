import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate

def schro(U,x):
    global E
    if x<1:
        V=-10
    else:
        V=0
    return [U[1],(V-E)*U[0]]

x=np.linspace(0,4,400)
#shooting method done manualy returns value:
E=-4.624185
phi=integrate.odeint(schro,[0,1],x)
print("Ground state energy: ",E," x  \u0127\u00b2/2ma\u00b2")
#finding normalisation factor by integration
norm=np.trapz(phi[:,0],x)
plt.plot(x,phi[:,0]/norm)
plt.xlabel("$x$"+" in multiples of a")
plt.ylabel(r"$\phi$")
plt.title("Ground state wavefunction")