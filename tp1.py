# ACTIVIDAD 1
print("Hello World")

# ACTIVIDAD 2
name = input("¿Cuál es tu nombre? ")
print(f"¡Hola,  {name}!")

# ACTIVIDAD 3
name = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
lugar = input("¿Dónde vives? ")
print(f"Soy {name}, tengo {edad} años y vivo en {lugar}.")

# ACTIVIDAD 4
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es: {area}, y el perímetro es: {perimetro}.")

# ACTIVIDAD 5
segundos = float(input("Ingrese el tiempo en segundos: "))
horas = segundos / 3600
print(f"El tiempo en horas es: {float(horas)} horas.")

# ACTIVIDAD 6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# ACTIVIDAD 7
numero1 = int(input("Ingrese el primer número distinto de 0: "))
numero2 = int(input("Ingrese el segundo número distinto de 0: "))
print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2}")
print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2}")
print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2}")
print(f"La división de {numero1} y {numero2} es: {numero1 / numero2}")

# ACTIVIDAD 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {IMC}")

# ACTIVIDAD 9
gradosC = float(input("Ingrese la temperatura en grados Celsius: "))
gradosF = (gradosC * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {gradosF}°C")

# ACTIVIDAD 10
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres números es: {int(promedio)}")


