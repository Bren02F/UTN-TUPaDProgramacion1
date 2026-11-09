#Actividad 1
productos = ["Lapicera,150.5,10\n"
    "Regla,100.0,15\n"
    "Cuaderno,300,30\n"]

with open("Unidad_8/Productos.txt", "w") as archivo:
    archivo.writelines(productos)

#Actividad 2
with open("Unidad_8/Productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Unidades: {partes[2]}")

#Actividad 3
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio: ")
unidad = input("Ingrese la cantidad: ")


nuevo_producto = f"{nombre},{precio},{unidad}\n"

with open("Unidad_8/Productos.txt", "a") as archivo:
    archivo.write(nuevo_producto)
productos = []

with open("Unidad_8/Productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
    
        producto= {"nombre": partes[0],
        "precio": float(partes[1]), 
        "cantidad": int(partes[2])}
        productos.append(producto)

print(productos)


busqueda= input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for product in productos:
    if product["nombre"].lower() == busqueda.lower():
        print(f"Producto encontrado:{product['nombre']} | Precio: ${product['precio']} | Cantidad: {product['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: El producto no existe en la lista") 

with open("Unidad_8/Productos.txt", "w") as archivo:


    for product in productos:
        linea = f"{product['nombre']},{product['precio']},{product['cantidad']}\n"
        archivo.write(linea)

print(f"Archivo 'Productos.txt' actualizado")