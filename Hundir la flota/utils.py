import numpy as np
import random


def crea_tablero(lado=10):
    tablero = np.full((lado, lado), "_")
    return tablero
# Creacion del tablero.


def coloca_barco_plus(tablero, barco):
    # Devuelve el tablero si puede colocar el barco; si no, devuelve False y avisa por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0 or fila >= num_max_filas:
            # print(f"No puedo poner la pieza {pieza} porque se sale del tablero") --> Comentado para ver si el juego se ve mas limpio.
            return False
        if columna < 0 or columna >= num_max_columnas:
            # print(f"No puedo poner la pieza {pieza} porque se sale del tablero")--> Comentado para ver si el juego se ve mas limpio.
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            # print(f"No puedo poner la pieza {pieza} porque hay otro barco")--> Comentado para ver si el juego se ve mas limpio.
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp
# utiliza una copia del tablero para ir agregando los barcos, no modifica el original, solo lo "mira" para saber si hay un barco.


def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Tocado")
        return "tocado"
    elif tablero[coordenada] == "X" or tablero[coordenada] == "A":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
        return "repetido"
    else:
        tablero[coordenada] = "A"
        print("Agua")
        return "agua"
# Sirve para disparar en el tablero creado y con las coordenadas dadas por el usuario y la CPU. Los return son para que el programa sepa que tiene que hacer despues.

def crea_barco_aleatorio(tablero, eslora=4, num_intentos=100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotético barco
        pieza_original = (random.randint(0, num_max_filas - 1), random.randint(0, num_max_columnas - 1))
        # print("Pieza original:", pieza_original) --> Comentado para ver si el juego se ve mas limpio.
        barco.append(pieza_original)
        orientacion = random.choice(["N", "S", "O", "E"])
        # print("Con orientacion", orientacion) --> Comentado para ver si el juego se ve mas limpio.
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora - 1):
            if orientacion == "N":
                fila -= 1
            elif orientacion == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila, columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        # print("Tengo que intentar colocar otro barco") --> Comentado para ver si el juego se ve mas limpio.
# Los barcos se ubican de manera aleatorio en el tablero, se van asignando a la lista vacia creada y si hay un barco ya creado prueba con otro. Es un barco a la vez.
# Si el barco no entra vuelve a sortear una casilla nueva y una orientacion.
# Devuele un tablero nuevo con el barco puesto. 


def colocar_barcos(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        tablero = crea_barco_aleatorio(tablero, eslora = eslora)
    return tablero
# Aca colocamos los barcos que nos pide el enunciado, tres de eslora dos, dos de eslora tres y uno de eslora cuatro.

def pedir_coordenada():
    while True:
        try:
            fila = int(input("Dame la coordenada de la fila: "))
            if fila in range(10):
                break
            else:
                print("Introduce un valor entre 0 y 9")
        except ValueError:
            print("Eso no es un numero. Por favor ingresa un numero valido")
    while True:
        try:
            columna = int(input("Dame la coordenada de la columna: "))
            if columna in range(10):
                break
            else:
                print("Introduce un valor entre 0 y 9")
        except ValueError:
            print("Eso no es un numero. Por favor ingresa un numero valido")
    return (fila, columna)
# Aca pedimos las coordenadas al usuario con un input y en caso de que ingrese un valor mayor que el tablero o una letra el bucle while se encarga de pedirle de nuevo hasta
# ingresar un valor correcto. Usamos try/except para poder solucionar en caso de ingresar un dato erroneo y en caso de los negativos.

def turno_usuario(tablero_cpu):
    while True:
        coordenada = pedir_coordenada()
        turno = recibir_disparo(tablero_cpu, coordenada)

        if turno == "agua":
            break
        elif (turno == "tocado") and (not quedan_barcos(tablero_cpu)):
            break 
# El usuario ingresa las coordenadas y se mostrara si acerto o no, en caso de agua se termina el turno y pasa al CPU y si es "tocado" se fija si aun quedan
# barcos por destruir y si acertas, seguis disparando. 

def coordenada_cpu(tablero):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    coordenada = (random.randint(0, num_max_filas - 1), random.randint(0, num_max_columnas - 1))
    return coordenada
# La CPU de manera aleatorio generara sus coordenadas.


def turno_cpu(tablero_usuario):
    while True:
        coordenada = coordenada_cpu(tablero_usuario)
        print(f"Ahora dispara CPU a {coordenada}")
        turno = recibir_disparo(tablero_usuario, coordenada)

        if turno == "agua":
            break
        elif (turno == "tocado") and ( not quedan_barcos(tablero_usuario)):
            break 
# La CPU usa las coordenadas y esto muestra si dio en el objetivo o no. Despues compara y en caso de que sea agua, pasa al usuario y si acierto, tocado,
# sigue jugando en caso de que queden aun barcos por destruir.

def quedan_barcos(tablero):
    compara1 = tablero == "O"
    compara2 = compara1.sum()
    barcos_restantes = compara2 >= 1

    return barcos_restantes
# Es para determinar si aun quedan barcos en el tablero o no.

def ocultar_barcos(tablero):
    vista = tablero.copy()
    vista[vista == "O"] = "_"
    return vista
# Es para ocultar los barcos de la CPU asi el usuario no los puede visualizar cada vez que se imprime por pantalla por eso se cambia el "O" por "_".
# Se trabaja sobre una copia para no perder los barcos.





