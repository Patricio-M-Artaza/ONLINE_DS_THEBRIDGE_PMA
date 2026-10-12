from utils import crea_tablero, colocar_barcos, turno_usuario, turno_cpu, quedan_barcos, ocultar_barcos

usuario = crea_tablero(10)
cpu = crea_tablero(10)

usuario = colocar_barcos(usuario)
cpu = colocar_barcos(cpu)

while True:
    vista_cpu = ocultar_barcos(cpu)

    print("TU TABLERO:")
    print(usuario)
    print("TABLERO ENEMIGO:")
    print(vista_cpu)

    turno_usuario(cpu)
    if not quedan_barcos(cpu):
        break
    turno_cpu(usuario)
    if not quedan_barcos(usuario):
        break

if quedan_barcos(usuario):
    print("GANO EL USUARIO!")
else:
    print("GANO LA CPU!")








