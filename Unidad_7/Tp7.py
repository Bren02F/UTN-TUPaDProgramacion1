# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Actividad 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)


# Actividad 3
frutas = list(precios_frutas.keys())
print("Lista de frutas sin precio:", frutas)



# Actividad 4
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto:")
    telefono = input("Ingrese el numero de telefono del contacto:")
    contactos[nombre] = telefono

print("\n---Consulta de contacto---")
nombre_consulta = input("Ingrese el nombre del contacto a consultar:")
if nombre_consulta in contactos:
    print(f"El numero de telefono de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontro el contacto {nombre_consulta} en la agenda.")



# Actividad 5
frase = input("Ingrese una frase:")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("\nPalabras únicas:", palabras_unicas)
print("Recuento:", recuento)




# Actividad 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)
print("Promedios")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio = {promedio:.2f}")




# Actividad 7
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 105, 106, 107}
ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)




# Actividad 8
stock_productos = {"Manzanas": 50, "Bananas": 30, "Peras": 20}
producto = input("Ingrese el nombre del producto: ").capitalize()
if producto in stock_productos:
    print(f"El stock actual de {producto} es: {stock_productos[producto]}")
    unidades = int(input("Ingrese cuántas unidades desea agregar al stock: "))
    stock_productos[producto] += unidades
else:
    print(f"El producto '{producto}' no existía en el inventario.")
    unidades = int(input("Ingrese el stock inicial para este nuevo producto: "))
    stock_productos[producto] = unidades
print("\nInventario actualizado:", stock_productos)





# Actividad 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Ingrese el día (ej: lunes): ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")
clave_busqueda = (dia, hora)
if clave_busqueda in agenda:
    print(f"Actividad programada: {agenda[clave_busqueda]}")
else:
    print("No hay ninguna actividad agendada para ese día y hora.")



# Actividad 10
    original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais  
print("Original:", original)
print("Invertido:", invertido)

