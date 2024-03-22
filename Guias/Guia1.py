import numpy as np
import matplotlib.pyplot as plt
import algorithms as alg

# Ejercicio 1
# 1.1
t, y = alg.senoidal(0,1,3,100,2,np.pi/2)
plt.subplot(2,3,1)
plt.stem(t,y)
plt.title("sen(x) fs=3")

t, y = alg.senoidal(0,1,13,100,2,np.pi/2)
plt.subplot(2,3,4)
plt.stem(t,y)
plt.title("sen(x) fs=13")

# 1.2
t, y = alg.sync(0,1,3,100)
plt.subplot(2,3,2)
plt.stem(t,y)
plt.title("sync(x) fs=3")

t, y = alg.sync(0,1,13,100)
plt.subplot(2,3,5)
plt.stem(t,y)
plt.title("sync(x) fs=13")

# 1.3
t, y = alg.square(0,1,3,100,np.pi/2)
plt.subplot(2,3,3)
plt.stem(t,y)
plt.title("square(x) fs=3")

t, y = alg.square(0,1,13,100,np.pi/2)
plt.subplot(2,3,6)
plt.stem(t,y)
plt.title("square(x) fs=13")


plt.show()

