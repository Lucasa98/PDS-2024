import numpy as np

def sin(Tini, Tfin, fs, A, phi, fm):
    """Muestre de una funcion senoidal

    Args:
        Tini (Float): instante inicial
        Tfin (Float): instante final (excluyente)
        fs (Float): frecuencia de la senial
        A (Float): amplitud
        phi (Float): desfase
        fm (Float): frecuencia de muestreo
    """
    T = 1/fm
    t = np.arange(Tini,Tfin-T,T)
    y = A*np.sin(2*np.pi*fs*t + phi)
    return t,y

def ruido(Tini, Tfin, A, fm, dens):
    T = 1/fm
    t = np.arange(Tini,Tfin-T,T)
    y = [0]*t
    for i in range(int(len(t)*dens)):
        y[int(i/dens)] = A * np.random.random_sample(1) - A/2
    return t,y

def suave(long, fm):
    T = 1/fm
    t = np.arange(T,2*long,T)
    phi = 3*np.pi/2
    y = 1+np.sin(np.pi*t/long + phi)
    return t,y

def cuadrada(Tini, Tfin, fs, A, long, esp):
    fm = (long+esp)*fs
    T = 1/fm
    t = np.arange(Tini,Tfin-T,T)
    y = [0]*len(t)
    i = 0
    while i < len(t):
        i += esp
        j = 0
        while i < len(t) and j < long:
            y[i] = A
            j += 1
            i += 1
    return t, y

