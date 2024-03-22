import numpy as np
import matplotlib.pyplot as plt

def senoidal (tini, tfin, fs, fm, A, phi):
    """ Ejercicio 1.1 - Generar senial senoidal discreta

    Args:
        tini (float): t inicial
        tfin (float): t final
        fs (float): frecuencia de la senial
        fm (float): frecuencia de muestreo
        A (float): amplitud
        phi (float): desfase
    """
    T = 1/fm
    t = np.arange(tini, tfin, T)
    y = A * np.sin(2 * np.pi * fs * t + phi)
    return t,y

def sync(tini, tfin, fs, fm):
    """ Ejercicio 1.2 - Generar senial sync discreta

    Args:
        tini (float): t inicial
        tfin (float): t final
        fs (float): frecuencia de la senial
        fm (float): frecuencia de muestreo
    """

    T = 1/fm
    t = np.arange(tini, tfin-T, T)
    y = np.sin(2 * np.pi * fs * t) / (2 * np.pi * fs * t)
    
    y[np.where(t==0)] = 1
    
    return t, y

def square(tini, tfin, fs, fm, phi):
    """ Ejercicio 1.3 - Generar onda cuadrada

    Args:
        tini (float): t inicial
        tfin (float): t final
        fs (float): frecuencia de la senial
        fm (float): frecuencia de muestreo
        phi (float): desfase
    """
    T = 1/fm
    t = np.arange(tini,tfin-T,T)
    y = np.sign(np.sin(2 * np.pi * fs * t + phi))
    
    return t, y