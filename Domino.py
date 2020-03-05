import pytest 

# Representaremos los valores de entrada del domino como tuplas; siendo:
# (numero1, numero2), (numero3, numnero3).
# encajan: Tuple Tuple -> Bool
# Toma dos tuplas y entrega True si encanjan, en caso contrario entrega
# False.
# Entrada: (3, 4), (4, 5); Salida: True.
# Entrada: (6, 6), (5, 5); Salida: False.
# Entrada: (2, 1), (2, 7); Salida: True.
def encajan(ficha1, ficha2):
    """Toma dos fichas del domino y determina si encajan o no."""
    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    return False

def test_encajan():
    assert encajan((3, 4), (4, 5)) == True
    assert encajan((6, 6), (5, 5)) == False
    assert encajan((2, 1), (2, 7)) == True

# Representaremos las fichas admitidas como tuplas, las cuales seran: del (0,0)
# al (6, 6).
# admitidas: Tuple -> Bool
# Toma una ficha y devuelve True si la misma esta admitida, en caso contrario
# entrega False.
# Entrada: (1, 1); Salida: True.
# Entrada: (9, 2); Salida: False.
# Entrada: (5, 6); Salida: True.
def admitidas(ficha):
    """Toma una ficha y entrega si la misma esta admitida."""
    if ficha[0] >= 0 and 6 >= ficha[0] and ficha[1] >= 0 and 6 >= ficha[1]:
        return True
    return False


def test_admitidas():
    assert admitidas((1, 1)) == True
    assert admitidas((9, 2)) == False
    assert admitidas((5, 6)) == True

# Representaremos cada ficha como una tupla
# generacion: None -> List
# Entrega una Lista con todas las fichas del domino en forma de tuplas.
# Entrada: None; Salida: ((0, 0), (0, 1), ... , (6, 6))
def generacion():
    """Devuelve una Tuple con todas las fichas del domino"""
    fichasDom = []
    for numero1 in range(0,7):
        for numero2 in range(0,7):
            fichasDom += (numero1, numero2),
    return fichasDom

def test_generacion():
    fichasDom = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
    assert generacion() == fichasDom

# Repreentaremos cada ficha como una tupla y al conjunto de fichas como una lista de tuplas.
# buscador: Tuple, List -> Bool
# Toma una ficha y una lista con fichas, devuelve un True si la ficha se encuentra en esa lista
# de fichas, en caso contrario devuelve un False.
# Entrada: (3, 6), [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0)]; Salida: False.
# Entrada: (1, 1), [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (6, 6)]; Salida: True.
# Entrada: (5, 5), [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 3)]; Salida: False.
def buscador(ficha, listFichas):
    """Entrega si la ficha se encuentra en esa lista de fichas."""
    for f in listFichas:
        if f == ficha:
            return True
    return False

def test_buscador():
    assert buscador((3, 6), [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0)]) == False
    assert buscador((1, 1), [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 1), (6, 6)]) == True
    assert buscador((5, 5), [(2, 0), (3, 1), (3, 2), (3, 3)]) == False
