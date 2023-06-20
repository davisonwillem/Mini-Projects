import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

res=200#int(input('Resolution (i.e. rxr): '))
x0=-1.5#float(input('X From: '))
x1=0.5#float(input('to: '))
y0=-1#float(input('Y From: '))
y1=1#float(input('to: '))

runs=10
resi=np.zeros((runs))
runtimes=np.zeros((runs))

for k in range (1,runs):
    start=time.time()
    res=k*200
    resi[k]=res
    manda=np.zeros((res,res,3),dtype=np.uint8)+255
        
    x=x0
    while x<x1:
        y=y0
        while y<y1:
            c=np.complex(x,y)
            z=c
            for i in range (1,20):
                z=z**2+c
                if np.absolute(z)>1e150:
                    #print("BREAK")
                    break
            if np.absolute(z)<1:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[0,0,0]
            elif np.absolute(z)<2:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,0,0]
            elif np.absolute(z)<1e6:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,0]
            elif np.absolute(z)<1e20:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,50]
            elif np.absolute(z)<1e50:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,100]
            elif np.absolute(z)<1e80:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,150]
            elif np.absolute(z)<1e120:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,200]
            elif np.absolute(z)<0.9*1e150:
                manda[int((y-y0)*(res/(y1-y0))),int((x-x0)*(res/(x1-x0)))]=[255,255,250] 
            y=y+(y1-y0)/res
        x=x+(x1-x0)/res
    
    plt.imshow(manda,interpolation='nearest')
    plt.show()
    #mand=Image.fromarray(manda,'RGB')
    #mand.save('mand.png')
    
    end=time.time()
    runtimes[k]=end-start

plt.figure()
plt.plot(resi,runtimes)
xex=np.arange(5000)
plt.plot(xex,np.poly1d((np.polyfit(resi,runtimes,2)))(xex))
plt.show()
print((np.poly1d((np.polyfit(resi,runtimes,2)))(10000))/60)