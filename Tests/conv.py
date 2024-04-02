import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
import algorithms as alg

long = 5

t,x = alg.cuadrada(0, long, 2, 1, 30,60)    # Senial x
#th,h = alg.suave(1,30)                      # Respuesta al impulso h

h = [0.1]*8
h.extend([1]*15)
h.extend([0.1]*7)

tr,r = alg.ruido(0, long, 0.1, 180,1/100)   # Ruido
xr = x#np.sum([x,r],axis=0)

y = np.convolve(xr,h,mode="same")            # Salida y=x*h
#yr = y+r                                    # Salida con ruido

xd1,remainder = sp.deconvolve(y,h)         # Senial x deconvolucinando yr

#con propositos de graficar
diff = int((len(x)-len(xd1))/2)

xd = [0]*len(t)
for i in range(len(xd1)):
    xd[i+diff] = xd1[i]
    
#--------------------------

f,(ax1,ax2,ax3,ax4) = plt.subplots(4,1,sharex=True)
ax1.set_xlim(0,5)
ax1.plot(t,x)
ax2.set_xlim(0,5)
ax2.plot(t,xr)
ax3.set_xlim(0,5)
ax3.plot(t,y)
ax4.set_xlim(0,5)
ax4.plot(t,xd)

plt.show()