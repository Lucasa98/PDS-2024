import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1
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

# Ejercicio 2
def invertir(y):
    """Ejercicio 2.1 Funcion que invierte una señal

    Args:
        y (NDArray[signedinteger[Any]]): señal
    """
    
    yinv = -y
    return yinv

def rectificar(y):
    """Ejercicio 2.2 Funcion que rectifica una señal

    Args:
        y (NDArray[signedinteger[Any]]): senial
    """
    
    yrect = y
    for i in range(len(yrect)):
        if yrect[i] < 0:
            yrect[i] = 0
    
    return yrect

def cuantificar(y,N):
    """Ejercicio 2.3 Funcion que cuantifica en N niveles

    Args:
        y (NDArray[signedinteger[Any]]): senial
        N (signedinteger): niveles
    """
    min_elem = min(y)
    H = (max(y)-min_elem)/(N-1)
    yquant = np.round((y-min_elem)/H)*H + min_elem
    
    return yquant

def round(t):
    if t > 0.999999:
        return 1.0
    return t

def Iescalon(t):
    """Funcion interpolante escalon

    Args:
        t (float): valor

    Returns:
        float: imagen
    """
    if 0 <= t and t < 1:
        return 1
    return 0

def Ilineal(t):
    """Funcion interpolante lineal

    Args:
        t (float): t

    Returns:
        float: x
    """
    if np.abs(t) < 1:
        return 1-np.abs(t)
    return 0

def Isinc(t):
    """Funcion interpolante sinc

    Args:
        t (float): t

    Returns:
        float: x
    """
    if t == 0:
        return 1
    return np.sin(np.pi * 0.5 * t)/(np.pi * 0.5 * t)

def interpolar(m, Ti, T, y, I):
    """Funcion interpoladora

    Args:
        m (signedinteger):                  numero de muestra en la senial interpolada
        Ti (float):                         periodo de la senial interpolada
        T (float):                          periodo de la senial original
        y (NDArray[signedinteger[Any]]):    valores de la funcion original
        I (function):                       funcion interpolante

    Returns:
        float: x(mTi) valor de la funcion interpolada
    """
    sum = 0
    for n in range(len(y)-1):               # n: numero de muestra en la senial original
        sum += y[n] * I(round((m * Ti - n * T) / T))
    return sum

def interpolar4X(t,y,interpolacion):
    """Funcion para sobremuestrar senial x4 usando interpolacion

    Args:
        t (NDArray[signedinteger[Any]]): dominio
        y (NDArray[signedinteger[Any]]): imagen (senial)
        interpolacion (function): funcion interpolante

    Returns:
        {NDArray[signedinteger[Any]], NDArray[signedinteger[Any]]}: ti, yi
    """
    T = t[1]-t[0]                       # periodo original
    Ti = T/4                            # periodo de la interpolacion
    ti = np.arange(min(t),max(t),Ti)    # muestreo de la interpolacion (4x)
    yi = [0]*len(ti)
    for m in range(len(ti)):
        yi[m] = interpolar(m,Ti,T,y,interpolacion)
    return ti, yi

def potencia(y):
    """Calcular potencia de una senial

    Args:
        y (NDArray[signedinteger[Any]]): senial discreta
    """
    sum = 0
    for i in range(len(y)):
        sum += np.power(y[i],2)
    return sum/len(y)
    