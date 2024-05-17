import numpy as np
import matplotlib.pyplot as plt

# Funcion norma-p
def pnorm(x,p):
  if p == np.inf:
    return max(np.abs(x))

  N = len(x)
  return np.power(np.sum(np.power(np.abs(x),[p]*N),axis=0),1/p)


# definimos la aproximacion de lengendre a partir de 4 coeficientes
# en valores t
def eval_leg4(t,x0,x1,x2,x3):
  N = len(t)
  return x0/np.sqrt(2) + x1*np.sqrt(3/2)*t + x2*np.sqrt(5/2)*(3*np.power(t,[2]*N)/2 - 0.5) + x3*np.sqrt(7/2)*(5*np.power(t,[3]*N)/2 - 3*t/2)

# funcion a aproximar
fm = 50
T = 1/fm
t = np.arange(-1,1,T)
N = len(t)

y = [0]*N
for n in range(N):
  if t[n] < 0:
    y[n] = -1
  else:
    y[n] = 1

leg = eval_leg4(t,0,np.sqrt(3/2),0,-np.sqrt(7/32))

# ------------------------ PLOT ------------------------
plt.figure(figsize=(15,10))

plt.plot(t,y, label="y(t)")
plt.plot(t,leg, label="Legendre")
plt.legend()

plt.text(-1,1,f'Error Cuad Total: {pnorm(y-leg,2)**2}')

plt.tight_layout()
plt.show()

# variacion de los coeficientes
t1 = np.arange(-0.1,0.1,0.01)

alpha1 = np.sqrt(3/2)
alpha2 = -np.sqrt(7/32)

xaxis = []
yaxis = []
z = [0]*(len(t1)**2)

for i in range(len(t1)):
  xaxis += [t1[i]]*len(t1)
  yaxis = np.append(yaxis,t1)
  for j in range(len(t1)):
      auxsignal = [0]*len(t)
      auxsignal = eval_leg4(t,0,alpha1+t1[i],0,alpha2+t1[j])
      z[len(t1)*i + j] = pnorm(y-auxsignal,2)**2

# ------------------------ Plot ------------------------
fig = plt.figure(figsize=(9, 15))

ax = fig.add_subplot(111, projection='3d')
cmhot = plt.get_cmap("winter")
ax.scatter(xaxis,yaxis,z,vmin=min(z),vmax=max(z),c=z,cmap=cmhot)
ax.set_xlabel('a1')
ax.set_ylabel('a2')
ax.set_zlabel('<x,y>')

plt.tight_layout()
plt.show()