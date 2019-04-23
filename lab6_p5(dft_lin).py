import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*k*n))
		y.append(abs(sum))
	
	return y

x1=input("enter x1 values")
x2=input("enter x2 values")
y1=dft(x1)
y2=dft(x2)
y=np.add(y1,y2)
x=np.add(x1,x2)
y0=dft(x)
print ('sum of individual two dft seq=',y)
print ('dft of sum of seq=',y0)
plt.subplot(2,1,1)
plt.xlabel('----->freq')
plt.ylabel('------>|x1[k]|+|x2(k)|')
plt.title('sum of DFT of x1,x2')
plt.stem(y)
plt.subplot(2,1,2)
plt.xlabel('----->freq')
plt.ylabel('------>|x[k]|')
plt.title('dft of seq x')
plt.stem(y0)
plt.show()
