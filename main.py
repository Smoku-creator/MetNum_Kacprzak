import numpy as np


def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0 and (type(h) is float) and (type(r) is float):
        return 2 * np.pi * r * (r + h)
    else:
        x = float('nan')
        return x

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if (n < 1) or (type(n) != int):
        return None
    elif n == 1:
        return np.array([1], dtype = int)
    elif n == 2:
        return np.array([1, 1], dtype = int)
    else:
        lst = np.ndarray(shape = (1, n), dtype = int)
        lst[0][0:2] = 1, 1
        for i in range(2, n):
            lst[0][i] = lst[0][i-1] + lst[0][i-2]
        return lst

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    m = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    mdet = np.linalg.det(m)
    mt = np.transpose(m)
    scr = float('NaN')
    if mdet == 0:
        return scr, mt, mdet
    else:
        return np.linalg.inv(m), mt, mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if (type(m) != int) or (type(n) != int) or (m < 0) or (n < 0):
        return None
    mat = np.zeros((m, n))
    for i in range(0, m):
        for j in range(0, n):
            if i <= j:
                mat[i][j] = j
            else:
                mat[i][j] = i
    return mat
    
    