# Librerias:
import pytest  # Libreria para casos de prueba 
from random import * # Libreria para utilizar las funciones de azar
#-----------------------------------------------------------------------------------------------
# Video de guia utilizado: 
#-----------------------------------------------------------------------------------------------
# Tabla exponencial de fichas en el domino(de la ficha mas chica a la mas grande):
# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3),
# (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4),
# (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]
# PD: ESTO SE BASA EN EL CONJUNTO DE FICHA DEL (0, 0) AL (6, 6)
#-----------------------------------------------------------------------------------------------
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
            if numero1 <= numero2:
                fichasDom += (numero1, numero2),
    return fichasDom

def test_generacion():
    fichasDom = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]
    assert generacion() == fichasDom

# Representaremos cada ficha como una tupla y al conjunto de fichas como una lista de tuplas.
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

# Representaremos las ficha como tupla y al conjunto de fichas como una lista de tuplas. Maximo
# de jugadores son 
# repartidor: Int Int List -> List
# Toma la cantidad de jugadores, la cantidad de fichas y una lista de tupla, devuelve una lista con fichas aleatorias.
# Entrada: 2, 3, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (5, 4), (5, 5), (5, 6), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]; Salida: [[(6, 1), (6, 6), (1, 1)], [(5, 5), (0, 4), (5, 6)]].
def repartidor(player, fichMax, listaFichas):
    """Entrega una lista con las fichas de cada jugador."""
    jugadores = []
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    jugador5 = []
    jugador6 = []
    jugador7 = []
    n = 0
    if player == 2:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            random2 = randint(0, len(listaFichas)-1)
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
        jugadores += jugador1, jugador2,
        return jugadores
    elif player == 3:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            random2 = randint(0, len(listaFichas)-1)
            random3 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
            jugador3 += listaFichas[random3],
            listaFichas[listaFichas.index(listaFichas[random3]):listaFichas.index(listaFichas[random3])+1] = []
        jugadores += jugador1, jugador2, jugador3,
        return jugadores
    elif player == 4:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            random2 = randint(0, len(listaFichas)-1)
            random3 = randint(0, len(listaFichas)-1)
            random4 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
            jugador3 += listaFichas[random3],
            listaFichas[listaFichas.index(listaFichas[random3]):listaFichas.index(listaFichas[random3])+1] = []
            jugador4 += listaFichas[random4],
            listaFichas[listaFichas.index(listaFichas[random4]):listaFichas.index(listaFichas[random4])+1] = []
        jugadores += jugador1, jugador2, jugador3, jugador4,
        return jugadores
    elif player == 5:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            random2 = randint(0, len(listaFichas)-1)
            random3 = randint(0, len(listaFichas)-1)
            random4 = randint(0, len(listaFichas)-1)
            random5 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
            jugador3 += listaFichas[random3],
            listaFichas[listaFichas.index(listaFichas[random3]):listaFichas.index(listaFichas[random3])+1] = []
            jugador4 += listaFichas[random4],
            listaFichas[listaFichas.index(listaFichas[random4]):listaFichas.index(listaFichas[random4])+1] = []
            jugador5 += listaFichas[random5],
            listaFichas[listaFichas.index(listaFichas[random5]):listaFichas.index(listaFichas[random5])+1] = []
        jugadores += jugador1, jugador2, jugador3, jugador4, jugador5,
        return jugadores
    elif player == 6:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            random2 = randint(0, len(listaFichas)-1)
            random3 = randint(0, len(listaFichas)-1)
            random4 = randint(0, len(listaFichas)-1)
            random5 = randint(0, len(listaFichas)-1)
            random6 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
            jugador3 += listaFichas[random3],
            listaFichas[listaFichas.index(listaFichas[random3]):listaFichas.index(listaFichas[random3])+1] = []
            jugador4 += listaFichas[random4],
            listaFichas[listaFichas.index(listaFichas[random4]):listaFichas.index(listaFichas[random4])+1] = []
            jugador5 += listaFichas[random5],
            listaFichas[listaFichas.index(listaFichas[random5]):listaFichas.index(listaFichas[random5])+1] = []
            jugador6 += listaFichas[random6],
            listaFichas[listaFichas.index(listaFichas[random6]):listaFichas.index(listaFichas[random6])+1] = []
        jugadores += jugador1, jugador2, jugador3, jugador4, jugador5, jugador6
        return jugadores
    elif player == 7:
        while n != fichMax:
            n += 1
            random1 = randint(0, len(listaFichas)-1)
            random2 = randint(0, len(listaFichas)-1)
            random3 = randint(0, len(listaFichas)-1)
            random4 = randint(0, len(listaFichas)-1)
            random5 = randint(0, len(listaFichas)-1)
            random6 = randint(0, len(listaFichas)-1)
            random7 = randint(0, len(listaFichas)-1)
            jugador1 += listaFichas[random1],
            listaFichas[listaFichas.index(listaFichas[random1]):listaFichas.index(listaFichas[random1])+1] = []
            jugador2 += listaFichas[random2],
            listaFichas[listaFichas.index(listaFichas[random2]):listaFichas.index(listaFichas[random2])+1] = []
            jugador3 += listaFichas[random3],
            listaFichas[listaFichas.index(listaFichas[random3]):listaFichas.index(listaFichas[random3])+1] = []
            jugador4 += listaFichas[random4],
            listaFichas[listaFichas.index(listaFichas[random4]):listaFichas.index(listaFichas[random4])+1] = []
            jugador5 += listaFichas[random5],
            listaFichas[listaFichas.index(listaFichas[random5]):listaFichas.index(listaFichas[random5])+1] = []
            jugador6 += listaFichas[random6],
            listaFichas[listaFichas.index(listaFichas[random6]):listaFichas.index(listaFichas[random6])+1] = []
            jugador7 += listaFichas[random7],
            listaFichas[listaFichas.index(listaFichas[random7]):listaFichas.index(listaFichas[random7])+1] = []
        jugadores += jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7
        return jugadores

# Representaremos las fichas del domino como tuplas y al conjunto de las mismas como una lista
# de tuplas.
# Reglas:
# · Cada jugador comenzara con 7 fichas
# · Cada jugador tendra un turno, luego seguira el de la derecha, es decir si fue el jugador1
#   luego tendra su turno el jugador2.
# · Empiza el jugador con la ficha mas alta, es decir si tenemos un (0, 9) y un (3, 0), se elejira
#   la ficha mas alta que es (3, 0), como se muestra en la tabla e fichas arriba.
# · El jugador debera ingresar un
# domino: Str -> Str
# Toma la cantidad de jugadores y los nombres, entrega las fichas y comienza el juego. El
# juego termina cuando el primero de los jugadores quede sin fichas. Entrega en forma de mensaje
# el juego a concluido con el nombre del ganador.
#
