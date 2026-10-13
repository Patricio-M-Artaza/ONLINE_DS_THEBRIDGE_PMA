from utils import crea_tablero, colocar_barcos, turno_usuario, turno_cpu, quedan_barcos, ocultar_barcos
# Importamos las funciones que vamos a usar.

usuario = crea_tablero(10)
cpu = crea_tablero(10)
# Creamos dos tableros, uno para usuario y otro para CPU.

usuario = colocar_barcos(usuario)
cpu = colocar_barcos(cpu)
# Colocamos los barcos de usuario y de CPU.

while True:
    vista_cpu = ocultar_barcos(cpu)
    print("*"*40)
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
# Ocultamos los barcos de la CPU para que el usuario no los pueda ver, se imprimen los tableros de ambos pero no se muestran los barcos del CPU.
# Primero dispara el usuario y luego la CPU, utilizo un break en ambos if ya que si el usuario hunde el ultimo barco de la CPU tiene que salir del bucle y sin ese
# break seguiria el turno de la CPU y podria ganar. 
# vista_cpu se tiene que armar dentro del bucle ya que en cada ronda hay que ocultar los barcos y si se arma fuera del bucle quedaria una sola imagen sin actualizar.

if quedan_barcos(usuario):
    print("GANO EL USUARIO!")
else:
    print("GANO LA CPU!")
# Si ya no quedan barcos de la CPU se imprime "GANO EL USUARIO!", caso contrario, se imprime "GANO LA CPU"
# Si yo tengo quedan_barcos(usuario) y pongo gano el usuario, esta bien, porque si quedan barcos quiere decir que la CPU ya no tiene barcos y viceversa.








