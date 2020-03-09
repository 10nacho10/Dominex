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
# (numero1, numero2), (numero3, numnero4).
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

# Representaremos los valores de entrada del domino como tuplas; siendo:
# (numero1, numero2), (numero3, numnero4).
# encajan: Tuple Tuple -> Bool
# Toma dos tuplas y entrega True si encanjan en la derecha, en caso contrario entrega
# False.
# Entrada: (1, 1), (1, 2); Salida: True.
# Entrada: (4, 5), (9, 4); Salida: False.
# Entrada: (0, 0), (0, 7); Salida: True.


def test_encajanD():
    assert encajanD((1, 1), (1, 2)) == True
    assert encajanD((4, 5), (9, 4)) == False
    assert encajanD((0, 0), (0, 7)) == True

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
def generacion(cantidad=6):
    """Devuelve una Tuple con todas las fichas del domino"""
    fichasDom = []
    for numero1 in range(0,cantidad+1):
        for numero2 in range(0,cantidad+1):
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
# · Cada jugador comenzara con 7 fichas.
# · Cada jugador tendra un turno, luego seguira el de la derecha, es decir si fue el jugador1
#   luego tendra su turno el jugador2.
# · Empieza el jugador con la ficha mas alta, es decir si tenemos un (0, 9) y un (3, 0), se elejira
#   la ficha mas alta que es (3, 0), como se muestra en la tabla e fichas arriba.
# · El jugador, luego que se halla ingresado la primera ficha en la mesa, debera ingresar una
#   ficha que coincida con la ingresada, es decir que si el jugador anterior coloco un (6, 6) y
#   nosotros tenemos un (3, 6) lo podemos colocar en la izquierda como en la derecha.
# · En caso de que algun jugador no tenga la ficha para colocar, ingrese "A" y le permitira
#   agarrar una ficha.
#   Ganador:
# · En caso que todas las fichas sobrantes se hayan acabado, los jugadores seguiran el juego
#   hasta que todos ingresen "T", cuando ingresen "T" el juego finalizara y sumara los puntos
#   del conjunto de fichas de los jugadores y vera quien es el que tiene la puntuacion mas baja.
#   El que obtenga una puntuacion menor a los contrincantes sera el ganador. En caso de empate
#   se decidira por medio aleatorio el ganador de los jugadores que empataron.
# · El juego tambien se puede ganar si alguno de los jugadores se queda con 0 fichas.
# domino: Str -> Str
# Toma la cantidad de jugadores y los nombres, entrega las fichas y comienza el juego. El
# juego termina cuando el primero de los jugadores quede sin fichas. Entrega en forma de mensaje
# el juego a concluido con el nombre del ganador.
def domino():
    puntosP1 = 0
    puntosP2 = 0
    m = 0
    fichasMesa = []
    print(" --------------------------------------------------------------------------")
    print("|                              ________                                    |")
    print("|                             |        |                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |        |                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |        |                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |--------|                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |        |                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |        |                                   |")
    print("|                             | O    O |                                   |")
    print("|                             |________|                                   |")
    print("|                                                                          |")
    print("|                                                                          |")
    print("|                      *Ingrese J para comenzar.                           |")
    print("|                                                                          |")
    print("|                      *Ingrese R para leer las reglas.                    |")
    print("|                                                                          |")
    print("|                      *Ingrese S para salir.                              |")
    print("|                                                                          |")
    print(" --------------------------------------------------------------------------")
    teclaIngresada = input(" Ingrese la opcion que desea realizar: ")
    if teclaIngresada == "R" or teclaIngresada == "r":
        print(" Reglas: \n· Cada jugador comenzara con 7 fichas.")
        print("· Cada jugador tendra un turno, luego seguira el de la derecha, es decir si fue el jugador1 \n  luego tendra su turno el jugador2.")
        print("· Empieza el jugador con la ficha mas alta, es decir si tenemos un (0, 9) y un (3, 0), se elejira \n  la ficha mas alta que es (3, 0), como se muestra en la tabla e fichas arriba.")
        print("  El jugador, luego que se halla ingresado la primera ficha en la mesa, debera ingresar una \n  ficha que coincida con la ingresada, es decir que si el jugador anterior coloco un (6, 6) y \n  nosotros tenemos un (3, 6) lo podemos colocar en la izquierda como en la derecha.")
        print("· En caso de que algun jugador no tenga la ficha para colocar, ingrese A y le permitira \n  agarrar una ficha.")
        print("  Ganador:")
        print("· En caso que todas las fichas sobrantes se hayan acabado, los jugadores seguiran el juego \n  hasta que todos ingresen T, cuando ingresen T el juego finalizara y sumara los puntos \n  del conjunto de fichas de los jugadores y vera quien es el que tiene la puntuacion mas baja. \n  El que obtenga una puntuacion menor a los contrincantes sera el ganador. En caso de empate \n  se decidira por medio aleatorio el ganador de los jugadores que empataron.")
        print("· El juego tambien se puede ganar si alguno de los jugadores se queda con 0 fichas.")
        return domino()
    elif teclaIngresada == "S" or teclaIngresada == "s":
        exit()
    elif teclaIngresada == "J" or teclaIngresada == "j":
        cantidadJugadores = int(input("Ingrese la cantidad de jugadores: "))
        cantidadFichas = int(input("Ingrese la cantidad de fichas que recibira cada jugador: "))
        de0acuanto = int(input("Ingrese el maximo de fichas, es decir del 0 al ....: "))
        fichasDom = generacion(de0acuanto)
        jugadores = repartidor(cantidadJugadores, cantidadFichas, fichasDom)
        sobrantes = fichasDom
        if cantidadJugadores == 2:
            player1 = jugadores[0]
            player2 = jugadores[1]
            print(player1)
            print(player2)
            turno = 1
            TeclaJuego = input("¿Comenzar a jugar? Y/N: ")
            if TeclaJuego == "n" or TeclaJuego == "N":
                return domino()
            elif TeclaJuego == "y" or TeclaJuego == "Y":
                while "T" != TeclaJuego or "t" != TeclaJuego:
                    if turno == 1:
                        print(" --------------------------------------------------------------------------")
                        print("|                                                                          |")
                        print("|                          |- - - - - - -|                                 |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                ", fichasMesa, "     |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                                                                          |")
                        print("|                             PLAYER1                                      |")
                        print("|                                                                          |")
                        print("|            ", player1, "            |")
                        print("|                                                                          |")
                        print("|                      * Ingrese S para salir.                             |")
                        print("|                      * Ingrese T para terminar.                          |")
                        print("|                      * Ingrese O para sacar una ficha.                                                    |")
                        print("|                      * Ingrese F para poner una ficha.                                                   |")
                        print("|                      * Ingrese P para pasar.                                                   |")
                        print(" --------------------------------------------------------------------------")
                        TeclaJuego = input("Ingrese alguna opcion: ")
                        if TeclaJuego == "s" or TeclaJuego == "S":
                            exit()
                        elif TeclaJuego == "T" or TeclaJuego == "t":
                            while len(player1) != m:
                                puntosP1 += player1[m][0] + player1[m][1]
                                puntosP2 += player2[m][0] + player2[m][1]  
                                m += 1
                            if puntosP1 > puntosP2:
                                print(" --------------------------------------------------------------------------")
                                print("|                                                                          |")
                                print("|                          |- - - - - - -|                                 |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                ", fichasMesa, "     |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                      EL GANADOR ES: PLAYER 1                             |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                      PUNTOS DE PLAYER 1:", puntosP1,    "                |")
                                print("|                      PUNTOS DE PLAYER 2:", puntosP2,    "                |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print(" --------------------------------------------------------------------------")
                                return "EL JUEGO HA FINALIZADO. GRACIAS POR JUGARLO :D"
                            elif puntosP2 > puntosP1:
                                print(" --------------------------------------------------------------------------")
                                print("|                                                                          |")
                                print("|                          |- - - - - - -|                                 |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                ", fichasMesa, "     |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                      EL GANADOR ES: PLAYER 2                             |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                      PUNTOS DE PLAYER 1:", puntosP1,    "                |")
                                print("|                      PUNTOS DE PLAYER 2:", puntosP2,    "                |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print("|                                                                          |")
                                print(" --------------------------------------------------------------------------")
                                return "EL JUEGO HA FINALIZADO. GRACIAS POR JUGARLO :D"
                            elif puntosP2 == puntosP1:
                                numAletorio = randint(0, 1)
                                if numAletorio == 0:
                                    print(" --------------------------------------------------------------------------")
                                    print("|                                                                          |")
                                    print("|                          |- - - - - - -|                                 |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                ", fichasMesa, "     |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                      EL GANADOR ES: PLAYER 1                             |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                      PUNTOS DE PLAYER 1:", puntosP1,    "                |")
                                    print("|                      PUNTOS DE PLAYER 2:", puntosP2,    "                |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print(" --------------------------------------------------------------------------")
                                    return "EL JUEGO HA FINALIZADO. GRACIAS POR JUGARLO :D"
                                else:
                                    print(" --------------------------------------------------------------------------")
                                    print("|                                                                          |")
                                    print("|                          |- - - - - - -|                                 |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                ", fichasMesa, "     |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                      EL GANADOR ES: PLAYER 2                             |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                      PUNTOS DE PLAYER 1:", puntosP1,    "                |")
                                    print("|                      PUNTOS DE PLAYER 2:", puntosP2,    "                |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print("|                                                                          |")
                                    print(" --------------------------------------------------------------------------")
                                    return "EL JUEGO HA FINALIZADO. GRACIAS POR JUGARLO :D"
                        elif TeclaJuego == "O" or TeclaJuego == "o":
                            if sobrantes == []:
                                print("                     No quedan mas fichas en la bolsa")
                            else:
                                player1 += sobrantes[0],
                        elif TeclaJuego == "F" or TeclaJuego == "f":
                            fichaIngresada = int(input("Ingrese el numero de la ficha que desea Ingresar. Por ej: 1 o 2 o 3. "))
                            if fichaIngresada <= len(player1)-1:
                                direccion = input("Elija la direccion donde desea colocar la ficha. ¿Izquierda o Derecha? I/D: ")
                                if direccion == "d" or direccion == "D":
                                    if fichasMesa[1] == player1[fichaIngresada-1][0]:
                                        fichasMesa += player1[fichaIngresada-1],
                                        player1[fichaIngresada-1:fichaIngresada] = []
                                        turno = 2
                                    else:
                                        print(" La ficha no encaja.")
                                        TeclaJuego = []
                                        while TeclaJuego != "R" or TeclaJuego != "r" or TeclaJuego != "T" or TeclaJuego != "t" or TeclaJuego != "S" or TeclaJuego != "s":
                                            print(" Elije alguna de esta opciones:\n * Ingrese R para rotar la ficha.\n * Ingrese T para pasar de turno.\n * Ingrese S para salir.")
                                            TeclaJuego = input("Ingrese que opcion desea realizar: ")
                                        if TeclaJuego != "R" or TeclaJuego != "r":
                                            fichaRotada = []
                                            fichaRotada += player1[fichaIngresada-1]
                                            player1[fichaIngresada-1:fichaIngresada] = []
                                            fichaRotada = list(fichaRotada)
                                            fichaRotada = fichaRotada.reverse()
                                        elif TeclaJuego != "T" or TeclaJuego != "t":
                                            turno = 2
                                        elif TeclaJuego != "S" or TeclaJuego != "s":
                                            exit()
                    elif turno == 2:
                        print("Hola")
            
            

