import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate

#%%#8.1

js=[1]
ps=[0]
dps=[-1]
dz=0.1
dzs=[0.1]

for i in range (200):
    dzs.append((i+1)*dz)
    jh=js[i]+0.5*dz*ps[i]
    ph=ps[i]+0.5*dz*dps[i]
    fjhph=-jh-ph/(dzs[i]+0.5*dz)
    js.append(js[i]+dz*ph)
    ps.append(ps[i]+dz*fjhph)
    dps.append(-js[i]-ps[i]/dzs[i])
#plt.plot(dzs,js)

def besdif(pnj,dzs):
    p=-(pnj[1]/dzs+pnj[0])
    return [pnj[1],p]
pnj0=[1,0]
vals=integrate.odeint(besdif,pnj0,dzs)
#plt.plot(dzs,vals[:,0])

#plt.plot(dzs,special.jv(0,dzs))

#%%#8.2

#theta=float(input("Enter an angle (0-90): "))
#while theta<0 or theta>90:
#    theta=input(float("Enter an angle (0-90): "))
theta=45
theta=theta*np.pi/180
t=np.linspace(0,20)
v0=[200*np.cos(theta),200*np.sin(theta)]

def cannondifx(v,t):
    ax=-(10**-4)*np.abs(v)*v[0]
    return ax
def cannondify(v,t):
    ay=-9.81-(10**-4)*np.abs(v)*v[1]
    return ay

vx=integrate.odeint(cannondifx,v0,t)
vy=integrate.odeint(cannondify,v0,t)

sx=0.5*vx[:,0]*t
sy=0.5*vy[:,1]*t

for i in range(50):
    if sy[49-i]<0:
        sx=np.delete(sx,49-i)
        sy=np.delete(sy,49-i)

#print(sx[np.size(sx)-1])
#plt.plot(sx,sy)

#%%#8.3

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