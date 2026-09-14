# Actividad 1
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for contador in range(0, 101):
    print(contador)

# Actividad 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero: "))

contador = 0

if numero == 0:
    contador = 1
else:
    contador = 0
while numero != 0:
    numero = numero // 10
    contador = contador + 1
print("El numero tiene", contador, "digitos")


# Actividad 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
conatdor = 0

for contador in range(num1 + 1, num2):
    # print(contador)
    suma = suma + contador

print("La sumatoria es: ", suma)

# Actividad 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numeros = int(input("Ingrese el número: "))
suma = 0

if numeros == 0:
    print(suma)
else:
    while numeros != 0:
        suma = suma + numeros
        numeros = int(input("Ingrese el número: "))
print("La sumatoria es: ", suma)

# Actividad 5
#  Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_random = random.randint(0,9)
intentos = 1
numero = int(input("Adivina el número entre 0 y 9. Ingresa el primer número: "))

if numero == numero_random:
    print("¡Adivinaste! El número correcto es", numero_random)
else:
    while numero != numero_random:
        numero = int(input("Equivocado. Ingresa otro número: "))
        intentos = intentos + 1
    print("¡Adivinaste! El número correcto es", numero_random)

print("Necesitaste", intentos, "intentos.")

# Actividad 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente

conatdor = 0
for contador in range(100, 0, -2):
    print(contador)


# Actividad 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingrese un número entero: "))
suma = 0

for contador in range(0, numero):
    # print(contador)
    suma = suma + contador

print("La sumatoria de los numeros entre 0 y", numero, "es", suma)


# Actividad 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos

cantidad_de_numeros = int(input("Ingrese la cantidad de numeros que desea analizar: "))

numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0

for contador in range(cantidad_de_numeros):
    numero_pedido = int(input("Ingrese el numero entero que desea analizar: "))
    if numero_pedido % 2 == 0:
        numeros_pares = numeros_pares + 1
    else: 
        numeros_impares = numeros_impares + 1
    if numero_pedido >= 0:
        numeros_positivos = numeros_positivos + 1
    else :
        numeros_negativos = numeros_negativos + 1

print("La cantidad de numeros par son:", numeros_pares)
print("La cantidad de numeros impar son:", numeros_impares)
print("La cantidad de numeros positivos son:", numeros_positivos)
print("La cantidad de numeros negativos son:", numeros_negativos)

# Actividad 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

cantidad_de_numeros = int(input("Ingrese la cantidad de numeros que desea utilizar: "))
suma = 0

for contador in range(cantidad_de_numeros):
    numero_ingresado = int(input("Ingrese el número:"))
    suma = suma + numero_ingresado
media = suma / cantidad_de_numeros
print("La media de los números ingresados es:", media)

# Actividad 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.

numero = int(input("Ingrese un número: "))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("El número invertido es:", invertido)