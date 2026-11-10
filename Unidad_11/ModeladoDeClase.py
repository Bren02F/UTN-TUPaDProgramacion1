class Autor:
    def __init__(self, id_autor,nombre,nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, id_libro, titulo, año_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor = autor 
        
def __str__(self):
        return f"Libro: {self.titulo} ({self.año_publicacion}) - {self.autor}"