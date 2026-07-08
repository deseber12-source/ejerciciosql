from database import conectar

conexion, cursor = conectar()

cursor.execute("SELECT * FROM libros")

for libro in cursor.fetchall():
    print(libro)

conexion.close()