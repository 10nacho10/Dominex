import pytest 

# Representaremos los valores de entrada del domino como tuplas; siendo:
# (numero1, numero2), (numero3, numnero3).
# encajan: Tuple Tuple -> True
# Toma dos tuplas y entrega True si encanjan, en caso contrario entrega
# False.
# Entrada: (3, 4), (4, 5); Salida: True.
# Entrada: (6, 6), (5, 5); Salida: False.
# Entrada: (2, 1), (2, 7); Salida: True.

def test_encajan():
    assert encajan((3, 4), (4, 5)) == True
    assert encajan((6, 6), (5, 5)) == False
    assert encajan((2, 1), (2, 7)) == True
