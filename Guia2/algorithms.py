import numpy as np

def sin(Tini, Tfin, fs, A, phi, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = A * np.sin(2 * np.pi * fs * t + phi)
    return t, y

def normal(Tini, Tfin, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = (1/np.sqrt(2*np.pi))*np.exp(-np.power(t,2)/2)
    return t,y