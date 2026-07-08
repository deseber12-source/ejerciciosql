from database import conectar

conexion, cursor = conectar()

#tabla de usuarios

cursor.execute ('''
CREATE TABLE IF NOT EXISTS usuarios (
usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
fecha_registro DATE DEFAULT CURRENT_DATE,
activo BOOLEAN DEFAULT 1
)
''')

#tabla de libros
cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
libro_id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
autor TEXT NOT NULL,
genero TEXT,
año_publicacion INTEGER,
disponible BOOLEAN DEFAULT 1,
fecha_agregado DATE DEFAULT CURRENT_DATE
)
''')

#tabla de prestamos, relacion con usuarios y libros
cursor.execute('''
CREATE TABLE IF NOT EXISTS prestamos (
prestamo_id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario_id INTEGER NOT NULL,
libro_id INTEGER NOT NULL,
fecha_prestamo DATE DEFAULT CURRENT_DATE,
fecha_devolucion DATE,
FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
FOREIGN KEY (libro_id) REFERENCES libros(libro_id)
)
''')

conexion.commit()
print('✅ Se crearon las tablas correctamente')
conexion.close()