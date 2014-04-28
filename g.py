#Integrantes:
#Rodriguez Martinez Luis Felipe
#Medina Reyes Marco Antonio
import sys
 
MAX = 1
MIN = -1
global tiragato
 
def minimax(tablero, jugador):
    global tiragato
 
    if terminajuego(tablero):
        return [ganador(tablero), 0]
 
    movimientos=[]
    for jugada in range(0,len(tablero)):
        if tablero[jugada] == 0:
            tableroaux=tablero[:]
            tableroaux[jugada] = jugador
 
            puntuacion = minimax(tableroaux, jugador*(-1))
            movimientos.append([puntuacion, jugada])
 
 
    if jugador == MAX:
        movimiento = max(movimientos)
        tiragato = movimiento[1]
        return movimiento
    else:
        movimiento = min(movimientos)
        return movimiento[0]
 
 
def terminajuego(tablero):
    no_tablas = False
    for i in range(0,len(tablero)):
        if tablero[i] == 0:
            no_tablas = True
 
    if ganador(tablero) == 0 and no_tablas:
        return False
    else:
        return True
 
 
def ganador(tablero):
    lineas = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    ganador = 0
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]
 
    return ganador
 
def ver_tablero(tablero):
    for i in range(0,3):
        for j in range(0,3):
            if tablero[i*3+j] == MAX:
                print('X'),
            elif tablero[i*3+j] == MIN:
                print('O'),
            else:
                print('.'),
 
        print('')
 
 
def juega_humano(tablero):
    ok=False
    while not ok:
        casilla = input ("Casilla?")
        if str(casilla) in '0123456789' and len(str(casilla)) == 1 and tablero[casilla-1] == 0:
            if casilla == 0:
                sys.exit(0)
            tablero[casilla-1]=MIN
            ok=True
    return tablero
 
 
def juega_ordenador(tablero):
    global tiragato
    punt = minimax(tablero[:], MAX)
    tablero[tiragato] = MAX
    return tablero
 
 
if __name__ == "__main__":
    print('Introduce casilla o 0 para terminar')
    tablero = [0,0,0,0,0,0,0,0,0]
 
    while (True):
        ver_tablero(tablero)
        tablero = juega_humano(tablero)
        if terminajuego(tablero):
            break
 
        tablero = juega_ordenador(tablero)
        if terminajuego(tablero):
            break
 
    ver_tablero(tablero)
    g = ganador(tablero)
    if g == 0:
        gana = 'Empate'
    elif g == MIN:
        gana = 'Humano'
    else:
        gana = 'Gato'
 
    print('Ganador:') + gana