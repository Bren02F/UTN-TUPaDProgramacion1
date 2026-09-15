
# Actividad 1
# Escribe un programa que permita al usuario ingresar una lista de numeros y calcule la suma de todos los elementos en la lista.

cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista = []
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
print(f"La suma de la lista es: {sum(lista)}")

# Actividad 2
# Escribe un programa que pida al usuario una lista de numeros y encuentre el mayor y el menor de ellos. 

cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista =[]
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
print(f"El número mayor de la lista es {max(lista)} y el número menor es {min(lista)}")

# Actividad 3
# Escribe un programa que permita al usuario ingresar una lista y la invierta. 
cantidad_de_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a su lista: "))
lista =[]
for contador in range(cantidad_de_elementos):
    print("Ingrese el valor: ")
    lista.append(int(input()))
lista.reverse()
print(lista)

# Actividad 4
# Escribe un programa que pida al usuario una lista de números y cuente cuántos de ellos son pares y cuántos son impares.

entrada = input("Ingrese numeros enteros separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

pares = sum(1 for x in numeros if x % 2 == 0)
impares = len(numeros) - pares

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)

# Actividad 5
# Escribe un programa que multiplique cada elemento de una lista de números por un valor ingresado por el usuario. 

entrada = input("Ingrese numeros separados por espacios: ")
numeros = [float(x) for x in entrada.split()]
factor = float(input("Ingrese el numero por el cual desea multiplicar: "))

resultado = [x * factor for x in numeros]
print("Lista multiplicada:", resultado)

# Actividad 6
# Escribe un programa que permita al usuario ingresar una lista de números y elimine los elementos duplicados.
entrada = input("Ingrese numeros separados por espacios: ")

lista_original = [] 
for x in entrada.split():
    lista_original.append(float(x))

sin_duplicados = set(lista_original)

print("Elementos sin duplicados:", sin_duplicados)


# Actividad 7
# Escribe un programa que permita al usuario ingresar una lista de números y calcule el promedio de los elementos.

entrada = input("Ingrese numeros separados por espacios:")

lista = list(map(int, entrada.split()))
suma = sum(lista)

promedio = suma / len(lista)
print("El promedio es:", promedio)

# Actividad 8
# Escribe un programa que identifique y muestre los elementos que se repiten en una lista. 
entrada = input("Ingrese los numeros separados por espacios:")
lista = list(map(int,entrada.split()))
repetidos = set()
for elemento in lista:
    if lista.count(elemento) > 1:
        repetidos.add(elemento)
print("Los elementos repetidos son:", repetidos)

# Actividad 9
# Escribe un programa que permita al usuario ingresar una lista de números y filtre los números primos. 

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
entrada = input("Ingrese numeros separados por espacios:")
lista = list(map(int,entrada.split()))
primos = []
for numero in lista:
    if es_primo(numero):
        primos.append(numero)
print("Los numeros primos son:", primos)

# Actividad 10
# Escribe un programa que permita al usuario ingresar una lista de números y eliminar un elemento en un índice especificado. 

entrada = input("Ingrese numeros separados por espacios:")
lista = list(map(int,entrada.split()))
indice = int(input("Ingrese el indice del elemento que desea eliminar:"))
if 0 <= indice < len(lista):
    lista.pop(indice)
    print("Lista actualizada:", lista)

# Actividad 11
# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente cuántas veces aparece ese número en la lista. 

entrada = input("Ingrese numeros separados por espacios:")

lista = list(map(int,entrada.split()))

numero_a_buscar = int(input("Ingrese el numero que desea buscar:"))

cantidad = lista.count(numero_a_buscar)

print(f"El numero {numero_a_buscar} aparece {cantidad} veces en la lista.")


# Actividad 12
# Escribe un programa que sume dos listas de números elemento por elemento. Las listas deben tener la misma longitud.

entrada1 = input("Ingrese la primera lista de numeros separados por espacios:")
lista1 = list(map(int,entrada1.split()))
entrada2 = input("Ingrese la segunda lista de numeros separados por espacios:")

lista2 = list(map(int,entrada2.split()))

if len(lista1) != len(lista2):
    print("Las listas deben tener la misma lengitud.")
else:
    suma_listas = [a + b for a, b in zip(lista1, lista2)]
    print("La suma de las listas es:", suma_listas)

# Actividad 13
# Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays 

import numpy as np
numbers13=np.array([10,20,30,40])
print(numbers13)

result13=numbers13*2
print(result13)

matriz13=np.array([[1,2,3], [4,5,6]])

print(matriz13)
print(matriz13[0][1])
matriz_b_13=np.array([[5,6,7], [7,8,9]])

result13=matriz13+matriz_b_13

print(result13)