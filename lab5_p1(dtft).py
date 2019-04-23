import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=10000
	n=len(x)
	p=np.linspace(0,2*np.pi,N)
	for i in range(0,N):
		w=p[i]
		sum=0
                     	for k in range(0,n):
            			sum=sum+(x[k]*np.exp(-j*w*k))
		y.append(abs(sum))
	return y
N=10000
p=np.linspace(0,2*np.pi,N)
x=input("enter x values")
t=dtft(x)
plt.xlabel('------>freq')
plt.ylabel('mag--|x**(jw)|')
plt.title('DTFT of given seq')
plt.plot(p,t)
plt.show()
  
