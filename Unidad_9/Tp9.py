class Archivo:
    def __init__(self, nombre:str, tamano_bytes:int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []

def calcular_tamano_total(directorio:Directorio) -> int:
    total = 0
    for archivo in directorio.archivos:
        total += archivo.tamano_bytes
    for subdirectorio in directorio.subdirectorios:
        total += calcular_tamano_total(subdirectorio)
    return total

def buscar_por_extension(directorio:Directorio, extension:str) -> list:
    archivos_encontrados = []
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            archivos_encontrados.append(directorio.nombre + "/" + archivo.nombre)
    for subdirectorio in directorio.subdirectorios:
        resultados = buscar_por_extension(subdirectorio, extension)
        for resultado in resultados:
            archivos_encontrados.append(directorio.nombre + "/" + resultado)
    return archivos_encontrados

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados = 0
    archivos_validos = []
    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            eliminados += 1
        else:
            archivos_validos.append(archivo)
    directorio.archivos = archivos_validos
    for subdirectorio in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(subdirectorio)
    return eliminados

def mostrar_arbol(directorio: Directorio, nivel: int = 0):
    prefijo = "  " * nivel
    print(f"{prefijo} {directorio.nombre}/")
    for archivo in directorio.archivos:
        print(f"{prefijo} {archivo.nombre} ({archivo.tamano_bytes} bytes)")
    for subdirectorio in directorio.subdirectorios:
        mostrar_arbol(subdirectorio, nivel + 1)


root = Directorio("root")
root.archivos.append(Archivo("documento.pdf", 1500))
root.archivos.append(Archivo("config.txt", 0))
root.subdirectorios.append(Directorio("imagenes"))
root.subdirectorios[0].archivos.append(Archivo("foto1.jpg", 2000))
root.subdirectorios[0].archivos.append(Archivo("foto2.jpg", 3500))
root.subdirectorios.append(Directorio("proyectos"))
root.subdirectorios[1].archivos.append(Archivo("avance.pdf", 800))
root.subdirectorios[1].subdirectorios.append(Directorio("temp"))
root.subdirectorios[1].subdirectorios[0].archivos.append(Archivo("log.txt", 0))


print(f"El tamaño total de los archivos es: {calcular_tamano_total(root)} bytes")
print("Archivos con extensión .pdf:")
print(buscar_por_extension(root, ".pdf"))
mostrar_arbol(root)
print(limpiar_archivos_vacios(root), "archivos vacíos eliminados.")
mostrar_arbol(root)