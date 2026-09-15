# Actividad 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

for contador in range(4, 101, 4):
    print(contador)

# Actividad 2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

elementos = ["comida", "gatos", "series", "cigarrillos", "musica"]


print("El penultimo elemento es:", elementos[-2])


# Actividad 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 

lista1 = []

palabra1 = "Hola"
palabra2 = "Como"
palabra3 = "Estas"

lista1.append(palabra1)
lista1.append(palabra2)
lista1.append(palabra3)

print(lista1)

# Actividad 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)


# Actividad 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# Primero se define la lista.
    numeros = [8, 15, 3, 22, 7] 
# Luego con la función max() se escanea la lista, buscando el valor numérico mayor y con .remove() se remyeve de la lista.
    numeros.remove(max(numeros))
# Luego se imprime la lista modificada por pantalla.
    print(numeros)


# Actividad 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros = []

for contador in range(10, 31, 5):
    numeros.append(contador)

print(numeros)
print(numeros[0:2])

# Actividad 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "caracol"
autos[2] = "babosa"

print(autos)

# Actividad 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)


# Actividad 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


# Actividad 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [[], [], [], []]

lista_anidada[0].append(15)
lista_anidada[1].append(True)
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada[3].append(False)

print(lista_anidada)

