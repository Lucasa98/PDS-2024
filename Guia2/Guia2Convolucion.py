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

# Ejercicio 3
a1 = 0.1
a2 = 0.5
a3 = 0.9

t = np.arange(-1, 1, 1/10)

x1 = [0]*(len(t))
x1[10] = a1
x1[11] = 1
x2 = [0]*(len(t))
x2[10] = a2
x2[11] = 1
x3 = [0]*(len(t))
x3[10] = a3
x3[11] = 1

# --------graficas--------
f, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(3,3,sharex=True, sharey=True)
# ------------------------


# X
ax1.stem(t,x1)
ax1.set_ylabel("x[n]")
ax1.set_title("a = 0.1")
ax2.stem(t,x2)
ax2.set_title("a = 0.5")
ax3.stem(t,x3)
ax3.set_title("a = 0.9")

# w1
hA1 = [0]*len(x1)
for i in range(len(hA1)):
    hA1[i] = np.sin(8*x1[i])

ax4.stem(t,hA1)
ax4.set_ylabel("w[n]")

# y1
y1 = [0]*len(hA1)
for i in range(len(y1)):
    y1[i] = np.power(a1,hA1[i])

ax7.plot(t,y1)
ax7.set_ylabel("y[n]")

# w2
hA2 = [0]*len(x2)
for i in range(len(hA2)):
    hA2[i] = np.sin(8*x2[i])

ax5.stem(t,hA2)

# y2
y2 = [0]*len(hA2)
for i in range(len(y2)):
    y2[i] = np.power(a2,hA2[i])

ax8.plot(t,y2)

# w3
hA3 = [0]*len(x3)
for i in range(len(hA3)):
    hA3[i] = np.sin(8*x3[i])

ax6.stem(t,hA3)

# y3
y3 = [0]*len(hA3)
for i in range(len(y3)):
    y3[i] = np.power(a3,hA3[i])

ax9.plot(t,y3)

plt.show()