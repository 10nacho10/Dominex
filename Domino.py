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
