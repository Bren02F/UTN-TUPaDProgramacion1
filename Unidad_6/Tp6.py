# Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# Actividad 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

# Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Actividad 4
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

# Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos_ingresados = int(input("Ingrese la cantidad de segundos:"))
horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos son equivalentes a {horas:.2f} horas.")

# Actividad 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
numero_usuario = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)

# Actividad 7
def operaciones_basicas(a, b):
    suma = a + b 
    resta = a - b 
    multiplicacion = a * b 
    division = a / b 
    return (suma, resta, multiplicacion, division)
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
s, r, m, d = operaciones_basicas(num1, num2)
print("Resultados de las operaciones ")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicacion: {m}")
print(f"Division: {d}")

# Actividad 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso_ingresado = float(input("Ingrese su peso en kilogramos: "))
altura_ingresada = float(input("Ingrese su altura en metros: "))
imc_resultado = calcular_imc(peso_ingresado, altura_ingresada)
print(f"Su indice de masa corporal (IMC) es: {imc_resultado:.2f}")

# Actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius son equivalentes a {temperatura_fahrenheit:.2f} grados Fahrenheit.")

# Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los numeros ingresados es: {promedio:.2f}")