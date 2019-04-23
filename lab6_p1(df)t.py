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
x=input("enter x values")
t=dft(x)
print t
plt.xlabel('----->N')
plt.ylabel('------>|x[k]|')
plt.title('DFT of given seq')
plt.stem(t)
plt.show()
