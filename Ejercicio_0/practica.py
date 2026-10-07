lista1 = [5, 8, 2, 9, 4]

#Imprimi cada numero multiplicado por 2

for x in lista1:
    print(x * 2)
# Sumar todos los numeros sin usar sum()
sumar = 0
for i in lista1:
    sumar += i
print(sumar)

# Sumar el primero con el ultimo de la lista.
print(lista1[0] + lista1[-1])

# Numeros mayores que 4.
contador = 0
for j in lista1:
    if j > 4:
        contador += 1
print(contador)

# Encuentra el numero mayor sin usar max()
numero_maximo = 0
for z in lista1:
    if z > numero_maximo:
        numero_maximo = z
print(numero_maximo)

lista2 = [-7, -3, -9]

# Encontrar el numero maximo sin max()
contador1 = lista2[0]
for y in lista2:
    if y > contador1:
        contador1 = y
print(contador1)

# Imprimir los multiplos de 3 de en 3 hasta llegar a 30.

multiplos = 3

while multiplos <= 30:
    print(multiplos)
    multiplos += 3

# Sumar solo los numeros impares

impares = 0

for x in lista1:
    if x % 2 != 0:
        impares += x
print(impares)  

# Con un while imprimir de 10 a 1, cuenta regresiva

cuenta_regresiva = 10

while cuenta_regresiva >= 1:
    print(cuenta_regresiva)
    cuenta_regresiva -= 1

nums = [5, 8, 2, 9, 4]

#Imprimir cuantos numeros pares hay.

numeros_pares = 0
for x in nums:
    if x % 2 == 0:
        numeros_pares += 1
print(numeros_pares)

# Imprimir cuantos numeros impares hay

numeros_impares = 0

for y in nums:
    if y % 2 != 0:
        numeros_impares += 1
print(numeros_impares) 

# Sumar los numeros del 1 al 10.

suma_numeros = 1
total = 0

while suma_numeros <= 10:
    total += suma_numeros
    suma_numeros +=1 
print(total)

# Sumar solo los numeros impares e imprimir el total. Necesito una variable para guardar la suma antes del bucle for, luego una condicion if dentro del bucle y
# imprimir el total por fuera del bucle externo, es decir, del for.
nums = [5, 8, 2, 9, 4]
suma = 0

for x in nums:
    if x % 2 != 0:
        suma += x
print(suma)

# Sumar los numeros del 1 al 6 e imprimir el total. Aca tengo que hacer una variable por fuera del while, el while ponerle la condicion para que sume todo e
# imprimir el total por fuera. 

contador = 1
suma = 0

while contador <= 6:
    suma += contador
    contador += 1
print(suma)

# Multipliar los numeros del 1 al 5 e imprimir. En este caso necesito dos variables ANTES del bucle while una para que vaya contando desde 1 hasta 5 y otra para ir
# guardando ese conteo e ir multiplicando.

contador1 = 1
multi = 1

while contador1 <= 5:
    multi *= contador1
    contador1 += 1

print(multi)


# Armar una lista nueva con el cuadrado de cada numero de una lista mayor a 5. En este caso tengo que tener dos variables: con una lista vacia antes del bucle for, otra que empiece
# con el indice 0 de la lista y se vaya multiplicando y por ultimo imprimir la nueva lista.

datos = [3, 8, 1, 10, 7]

lista_vacia = []

for x in datos:
    if x > 5:
        lista_vacia.append(x ** 2)

print(lista_vacia)

# Tengo que modificar la lista para que cada numero negativo pase a ser 0 e imprimir esa misma lista. Aca no necesito ninguna variable antes ya que tengo que recorrer
# esa misma lista e imprimir directamente.

valores = [4, -2, 7, -9, 0]

for x in range(len(valores)):
    if valores[x] < 0:
        valores[x] = 0
print(valores)

import numpy as np
print(np.__version__)



