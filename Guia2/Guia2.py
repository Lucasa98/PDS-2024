import algorithms as alg
import matplotlib.pyplot as plt

# Ejercicio 1
t,x1 = alg.sin(-2,2,3,2,0,50)
t,x2 = alg.normal(-2,2,50)

y11 = x1 * x1
y12 = x1 * x2

plt.subplot(4,1,1)
plt.stem(t,x1)
plt.subplot(4,1,2)
plt.stem(t,y11)
plt.subplot(4,1,3)
plt.stem(t,x2)
plt.subplot(4,1,4)
plt.stem(t,y12)

plt.show()