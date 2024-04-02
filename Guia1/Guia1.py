import numpy as np
import matplotlib.pyplot as plt
import algorithms as alg
from scipy.stats import gaussian_kde

# Ejercicio 1
# 1.1
'''
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
'''

# Ejercicio 2
# 2.1
'''
t, y = alg.senoidal(0,1,3,100,2,np.pi/2)

plt.subplot(2,2,1)
plt.stem(t,y)

yinv = alg.invertir(y)

plt.subplot(2,2,2)
plt.stem(t, yinv)

# 2.2
t, y = alg.senoidal(0,1,3,100,2,np.pi/2)
yrect = alg.rectificar(y)

plt.subplot(2,2,3)
plt.stem(t,yrect)

# 2.3
t, y = alg.senoidal(0,1,3,100,2,np.pi/2)
yquant = alg.cuantificar(y,8)

plt.subplot(2,2,4)
plt.stem(t,yquant)

plt.show()
'''

# Ejercicio 3
'''
# Amplitud              = 3
# Fase                  = - 2 * pi * 20 * 5/800 = -pi/4 = 3pi/4
# Frecuecia             = 20
# Frecuencia de muestreo= 800
# Periodo de muestreo   = 1/800

t, y = alg.senoidal(0, 0.1, 20, 800, 3, -np.pi/4)
plt.stem(t,y)
plt.show()
'''

# Ejercicio 4
'''
t, y = alg.senoidal(0,1,5,100,2,0)
plt.subplot(3,2,1)
plt.title("100 Hz")
plt.stem(t,y)

t, y = alg.senoidal(0,1,5,25,2,0)
plt.subplot(3,2,2)
plt.title("25 Hz")
plt.stem(t,y)

t, y = alg.senoidal(0,1,5,10,2,0)
plt.subplot(3,2,3)
plt.title("10 Hz")
plt.stem(t,y)

t, y = alg.senoidal(0,1,5,4,2,0)
plt.subplot(3,2,4)
plt.title("4 Hz")
plt.stem(t,y)

t, y = alg.senoidal(0,1,5,1,2,0)
plt.subplot(3,2,5)
plt.title("1 Hz")
plt.stem(t,y)

t, y = alg.senoidal(0,1,5,0.5,2,0)
plt.subplot(3,2,6)
plt.title("0.5 Hz")
plt.stem(t,y)

plt.show()

# Los unicos casos en los que la cantidad de ciclos corresponde
# con la frecuencia de 5Hz es con 100 y 25 Hz. En el resto de casos
# se observan discrepancias debido a que no se cumple el teorema
# de la frecuencia de muestreo y se produce un efecto de Aliasing
'''

# Ejercicio 5
'''
t, y = alg.senoidal(0,2,4000,129,2,0)
plt.stem(t,y)
plt.show()

# La onda que se observa tiene una frecuencia de 1 Hz. Esto se debe
# a la relacion entre la frecuencia de muestreo y la frecuencia de la onda
# que se quiere muestrear, que produce un efecto de Aliasing, confundiendo
# la frecuencia real
'''

# Ejercicio 6

f, (ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)

t, y = alg.senoidal(0,2,2,10,2,0)

ti,yi = alg.interpolar4X(t,y,alg.Iescalon)
#----------------------------
for i in range(len(yi)):
    print(i, "  ", yi[i])
#----------------------------
ax1.stem(t,y)
markerline, stemlines, baseline = ax1.stem(ti,yi, linefmt='grey', markerfmt='D')
markerline.set_markerfacecolor('none')
ax1.set_title("Iescalon")

ti,yi = alg.interpolar4X(t,y,alg.Ilineal)
ax2.stem(t,y)
markerline, stemlines, baseline = ax2.stem(ti,yi, linefmt='grey', markerfmt='D')
markerline.set_markerfacecolor('none')
ax2.set_title("ILineal")

ti,yi = alg.interpolar4X(t,y,alg.Isinc)
ax3.stem(t,y)
markerline, stemlines, baseline = ax3.stem(ti,yi, linefmt='grey', markerfmt='D')
markerline.set_markerfacecolor('none')
ax3.set_title("Isinc")

plt.show()

# ejercicio 7
'''
fig = plt.figure()

# muestra
t = np.arange(0,50,1)
y = np.random.normal(0.0,1.0,50)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax1.plot(t,y)
ax1.spines.bottom.set_position('zero')

kde = gaussian_kde(y)
x = np.linspace(y.min(), y.max(), 1000)
ax = plt.subplot2grid((3, 3), (0, 2))
ax.plot(kde(x), x)
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

t = np.arange(0,100,1)
y = np.random.normal(0.0,1.0,100)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.plot(t,y)
ax2.spines.bottom.set_position('zero')

kde = gaussian_kde(y)
x = np.linspace(y.min(), y.max(), 1000)
ax = plt.subplot2grid((3, 3), (1, 2))
ax.plot(kde(x), x)
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

t = np.arange(0,300,1)
y = np.random.normal(0.0,1.0,300)
ax3 = plt.subplot2grid((3, 3), (2, 0), colspan=2)
ax3.plot(t,y)
ax3.spines.bottom.set_position('zero')

kde = gaussian_kde(y)
x = np.linspace(y.min(), y.max(), 1000)
ax = plt.subplot2grid((3, 3), (2, 2))
ax.plot(kde(x), x)
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()
'''

# Ejercicio 8
'''
t, y = alg.senoidal(0,2,3,100,2,0)
yr = np.random.rand(len(t))-0.5

ax1 = plt.subplot2grid((2,2), (0,0))
ax1.stem(t,y)
ax1.spines.left.set_position('zero')

ax2 = plt.subplot2grid((2,2), (0,1))
ax2.stem(t,yr)
ax2.spines.left.set_position('zero')

ax = plt.subplot2grid((2,2), (1,0), colspan=2)
ax.stem(t,y+yr)
ax.spines.left.set_position('zero')

print("potencia de la senial: ", alg.potencia(y))
print("potencia del ruido: ", alg.potencia(yr))
print("SNR = ", alg.potencia(y)/alg.potencia(yr))

yr = yr*2
print("2*ruido = ", alg.potencia(yr))
print("SNRnuevo = ", alg.potencia(y)/alg.potencia(yr))

plt.show()

# el valor de potencia del ruido para que la SNR resultante
# sea de 0 dB debe ser igual a la potencia de la senial
# log(1) = 0
'''