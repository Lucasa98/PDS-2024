import algorithms as alg
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sp

# Ejercicio 1
"""
def conv(x,h):
    # zeros (filas, columnas)
    H = np.zeros((len(x)+len(h)-1,len(x)))
    for i in range(len(x)+len(h)-1):
        for j in range(max(0,i-len(h)+1),min(i+1,len(x))):
            try:
                H[i][j] = h[i-j]
            except Exception as e:
                print("ERROR: i=",i,", j=",j, e)
    return np.matmul(H,x)

t,h = alg.suave(0.5,50)
x = [0]*200
for i in range(75,125):
    x[i] = 1

A = [1]
B = h

plt.subplot(5,1,1)
plt.stem(x)
plt.subplot(5,1,2)
plt.plot(t,h)
plt.subplot(5,1,3)
plt.plot(conv(x,h))
plt.subplot(5,1,4)
plt.plot(np.convolve(x,h))
plt.subplot(5,1,5)
plt.plot(sp.lfilter(B,A,x))

plt.show()
"""

# Ejercicio 2
"""
def convCirc(x,h):
    if len(x) == len(h):
        N = len(x)
        y = [0]*len(x)
        for n in range(len(x)):
            for l in range(len(x)):
                y[n] += h[l]*x[((N+n-l)%N)]
        return y

t,h = alg.suave(2,50)
x = [0]*len(t)
for i in range(75,125):
    x[i] = 1

y = convCirc(x,h)

plt.subplot(3,1,1)
plt.plot(t,x)
plt.title("x")
plt.subplot(3,1,2)
plt.plot(t,h)
plt.title("h")
plt.subplot(3,1,3)
plt.plot(t,y)
plt.title("convCirc")

plt.show()
"""

