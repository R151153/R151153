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
def dfttd(x,l):
	j=cm.sqrt(-1)
	y=[ ]
	N=len(x)
	for k in range(0,N):
		w=((2*np.pi)/N)
		sum=0
		for n in range(0,N):
			sum=sum+(x[n]*np.exp(-j*w*k*n))
			s1=np.exp(-j*w*k*l)
			sum=sum*s1
		y.append(abs(sum))
	
	return y
x=input("enter x values")
l=input('time delay=')
t1=dft(x)
t2=dfttd(x,l)
print t1
print t2
plt.subplot(2,1,1)
plt.xlabel('----->N')
plt.ylabel('------>|x[k]|')
plt.title('DFT of given seq')
plt.stem(t1)
plt.subplot(2,1,2)
plt.xlabel('----->N')
plt.ylabel('------>|x[k].e**(-jwkl)|')
plt.title('DFT of time delay of given seq')
plt.stem(t2)
plt.show()
