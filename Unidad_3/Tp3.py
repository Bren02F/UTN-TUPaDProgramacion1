#Actividad 1
adulto = int(input("Ingrese su edad: "))
if adulto >=18:
    print("Usted es un adulto")

#Actividad 2
    nota = int(input("Ingrese su nota: "))
if nota >=6:
    print("Usted está un aprobado")
else: 
    print("Usted está desaprobado")


#Actividad 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Actividad 4
edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Usted es un niño/a")
elif edad >=12 and edad < 18:
    print("Usted es un adoloscente")
elif edad >=18 and edad < 30:
    print("Usted es un adulto/a joven")
elif edad >=30:
    print("Usted es un adulto/a")


#Actividad 5
contraseña = input("Ingrese su contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña válida")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Actividad 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
numeromean = mean(numeros_aleatorios)
numeromode = mode(numeros_aleatorios)
numeromedian = median(numeros_aleatorios)

if numeromean < numeromedian and numeromean < numeromode:
    print("El sesgo es positivo")
elif numeromean > numeromedian and numeromean > numeromode:
    print("El sesgo es negativo")
else:
    print("No hay sesgo")


#Actividad 7
palabra = input("Ingrese una palabra: ")
if palabra[-1] == ("a") or palabra[-1] == ("e") or palabra[-1] == ("i") or palabra[-1] == ("o") or palabra[-1] == ("u"):
    print(f"{palabra}!")
else:
    print(f"{palabra}")


#Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 para poner el nombre en mayúscula, 2 para ponerlo en minúscula o 3 para ponerlo con la primera letra en mayúscula: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())



#Actividad 9
magnitud = int(input("Ingrese una magnitud: "))
if magnitud < 3:
    print("Sismo muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Sismo leve")
elif magnitud >= 4 and magnitud < 5:
    print("Sismo moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Sismo fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Sismo muy fuerte")
elif magnitud >= 7:
    print("Sismo extremo")


#Actividad 10
dia = int(input("Ingrese la fecha actual:"))
mes = input("Ingrese el mes actual: ")
hemisferio = input("Ingrese el hemisferio en el que se encuentra (Norte o Sur): ")
hemisferio = hemisferio.lower()
mes = mes.lower()
if hemisferio == "sur":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        print("Estamos en verano")
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        print("Estamos en otoño")
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        print("Estamos en invierno")
    elif mes == "septiembre" and dia >= 21 or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and dia <= 20:
        print("Estamos en primavera")
elif hemisferio == "norte":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        print("Estamos en invierno")
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        print("Estamos en primavera")
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        print("Estamos en verano")
    elif mes == "septiembre" and dia >= 21 or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and dia <= 20:
        print("Estamos en otoño")

