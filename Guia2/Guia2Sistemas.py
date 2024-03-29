import algorithms as alg
import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 1
"""
t1,x1 = alg.sin(-1,1,3,2,0,50)   # senial 1
t2,x2 = alg.normal(-2,2,50)      # senial 2

'''
causal:         y[n] depende de x[n] o y[n-1], etc...
lineal          ->  homogeneidad: x[n]->y[n] => ax[n]->ay[n]
                ->  superposicion: x1[n]->y1[n] ^ x2[n]->y2[n]
                                    => x1[n]+x2[n]->y1[n]+y2[n]
invariable:     x[n]->y[n] => x[n-k]->y[n-k]
con memoria:    y[n] depende de un y[n-k]
'''

# 1.1
# causal, lineal, variable en el tiempo, sin memoria
taux,xaux = alg.sin(-2,2,3,2,0,50)
y11 = x1 * x1
y12 = xaux * x2

# 1.2
#
'''
y21 = [0]*len(t1)
for n in range(len(y21)):
    for k in range(n-no,n+no+1):
        y21[n] += x1[k]

y22 = [0]*len(t2)
for n in range(len(y22)):
    for k in range(n-no,n+no+1):
        y22[n] += x2[k]
'''

# 1.3
# causal, no-lineal, invariable en el tiempo, sin memoria
y31 = x1 + 2
y32 = x2 + 2

# 1.4
# causal, lineal, variable en el tiempo, sin memoria
y41 = [0]*len(t1)
y42 = [0]*len(t2)
for n in range(len(t1)):
    y41[n] = n*x1[n]
for n in range(len(t2)):
    y42[n] = n*x2[n]


# x1
ax = plt.subplot2grid((4, 4),(0, 0), colspan=4)
ax.stem(t1,x1)

ax = plt.subplot2grid((4, 4), (1, 0))
markerline, stemline, baseline, = ax.stem(t1,y11)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

'''
ax = plt.subplot2grid((4, 4), (1, 1))
markerline, stemline, baseline, = ax.stem(t1,y21)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)
'''

ax = plt.subplot2grid((4, 4), (1, 2))
markerline, stemline, baseline, = ax.stem(t1,y31)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

ax = plt.subplot2grid((4, 4), (1, 3))
markerline, stemline, baseline, = ax.stem(t1,y41)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

# x2
ax = plt.subplot2grid((4, 4),(2, 0), colspan=4)
ax.stem(t2,x2)

ax = plt.subplot2grid((4, 4), (3, 0))
markerline, stemline, baseline, = ax.stem(t2,y12)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

'''
ax = plt.subplot2grid((4, 4), (3, 1))
markerline, stemline, baseline, = ax.stem(t2,y22)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)
'''

ax = plt.subplot2grid((4, 4), (3, 2))
markerline, stemline, baseline, = ax.stem(t2,y32)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

ax = plt.subplot2grid((4, 4), (3, 3))
markerline, stemline, baseline, = ax.stem(t2,y42)
plt.setp(stemline, linewidth = 1)
plt.setp(markerline, markersize = 3)

plt.show()
"""

# Ejercicio 2
"""
# y[n] = np.sqrt(np.power(x[n],2) + np.power(x[n-1],2) - 2*x[n]*x[n-1])
t,x1 = alg.sin(-2,2,2,1,0,50)
t,x2 = alg.normal(-2,2,50)
y1 = [0]*len(t)
y2 = [0]*len(t)
y1[0]=np.sqrt(np.power(x1[0],2) + np.power(x1[len(t)-1],2) - 2*x1[0]*x1[len(t)-1])
y2[0]=np.sqrt(np.power(x2[0],2) + np.power(x2[len(t)-1],2) - 2*x2[0]*x2[len(t)-1])
for n in range(1,len(t)):
    y1[n]=np.sqrt(np.power(x1[n],2) + np.power(x1[n-1],2) - 2*x1[n]*x1[n-1])
    y2[n]=np.sqrt(np.power(x2[n],2) + np.power(x2[n-1],2) - 2*x2[n]*x2[n-1])

plt.subplot(4,1,1)
plt.stem(t,x1)
plt.subplot(4,1,2)
plt.stem(t,y1)
plt.subplot(4,1,3)
plt.stem(t,x2)
plt.subplot(4,1,4)
plt.stem(t,y2)

plt.show()
"""

# Ejercicio 3
"""
# y[n] = x[n] + 0.5*y[n-1] - 0.25*y[n-2]
t,x1 = alg.sin(-2,2,2,1,0,50)
t,x2 = alg.normal(-2,2,50)

y1 = [0]*len(t)
y1[0] = 0
y1[1] = 0
y2 = [0]*len(t)
y2[0] = 0
y2[1] = 0
for n in range(2,len(t)):
    y1[n] = x1[n] + 0.5*y1[n-1] - 0.25*y1[n-2]
    y2[n] = x2[n] + 0.5*y2[n-1] - 0.25*y2[n-2]

plt.subplot(4,1,1)
plt.stem(t,x1)
plt.subplot(4,1,2)
plt.stem(t,y1)
plt.subplot(4,1,3)
plt.stem(t,x2)
plt.subplot(4,1,4)
plt.stem(t,y2)

plt.show()
"""

# Ejercicio 4
t = np.arange(-1,1-1/50,1/50)
x = [0]*len(t)
x[50] = 1

# y1[n] = x[n] + y1[n-2]
# y2[n] = x[n] + 0.5*x[n-1]
# y3[n] = x[n] + 0.5*y[n-1] - 0.25*y[n-2]

y1 = [0]*(len(t))
y2 = [0]*(len(t))
y3 = [0]*(len(t))
for n in range(2,len(t)):
    y1[n] = x[n] + y1[n-2]
    y2[n] = x[n] + 0.5*x[n-1]
    y3[n] = x[n] + 0.5*y3[n-1] - 0.25*y3[n-2]

plt.subplot(4,1,1)
plt.stem(t,x)
plt.subplot(4,1,2)
plt.stem(t,y1)
plt.subplot(4,1,3)
plt.stem(t,y2)
plt.subplot(4,1,4)
plt.stem(t,y3)

plt.show()