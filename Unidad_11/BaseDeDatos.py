import sqlite3

def inicializar_base_datos():
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, nacionalidad TEXT NOT NULL)")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, anio INTEGER NOT NULL, autor_id INTEGER, FOREIGN KEY (autor_id) REFERENCES autores(id))")
    
    conexion.commit()
    conexion.close()
    print("Base de datos 'biblioteca.db' inicializada con éxito")

if __name__ == "__main__":
    inicializar_base_datos()
    inicializar_base_datos()