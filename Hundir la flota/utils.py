import numpy as np
import random


def crea_tablero(lado=10):
    tablero = np.full((lado, lado), "_")
    return tablero


def coloca_barco_plus(tablero, barco):
    # Devuelve el tablero si puede colocar el barco; si no, devuelve False y avisa por pantalla
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0 or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna < 0 or columna >= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp


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


def crea_barco_aleatorio(tablero, eslora=4, num_intentos=100):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        # Construimos el hipotético barco
        pieza_original = (random.randint(0, num_max_filas - 1), random.randint(0, num_max_columnas - 1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N", "S", "O", "E"])
        print("Con orientacion", orientacion)
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
        print("Tengo que intentar colocar otro barco")

def colocar_barcos(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        tablero = crea_barco_aleatorio(tablero, eslora = eslora)
    return tablero

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

def turno_usuario(tablero_cpu):
    while True:
        coordenada = pedir_coordenada()
        turno = recibir_disparo(tablero_cpu, coordenada)

        if turno == "agua":
            break
        elif (turno == "tocado") and (not quedan_barcos(tablero_cpu)):
            break 

def coordenada_cpu(tablero):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    coordenada = (random.randint(0, num_max_filas - 1), random.randint(0, num_max_columnas - 1))

    return coordenada


def turno_cpu(tablero_usuario):
    while True:
        coordenada = coordenada_cpu(tablero_usuario)
        print(f"Ahora dispara CPU a {coordenada}")
        turno = recibir_disparo(tablero_usuario, coordenada)

        if turno == "agua":
            break
        elif (turno == "tocado") and ( not quedan_barcos(tablero_usuario)):
            break 

def quedan_barcos(tablero):
    compara1 = tablero == "O"
    compara2 = compara1.sum()
    barcos_restantes = compara2 >= 1

    return barcos_restantes




