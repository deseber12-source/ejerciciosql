import sqlite3

conexion = sqlite3.connect("basededatos.db")
cursor = conexion.cursor()

print('✅ Se creo base de datos correctamente')

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

# Se insertan usuarios de ejemplo:

usuarios = [
    ('Ana García', 'ana@email.com'),
    ('Carlos López', 'carlos@email.com'),
    ('María Rodríguez', 'maria@email.com'),
    ('Pedro Sánchez', 'pedro@email.com')
]

cursor.executemany('''
INSERT INTO usuarios (nombre, email) VALUES (?, ?)
''', usuarios)

# se insertan libros de ejemplo:

libros = [
    ('Cien Años de Soledad', 'Gabriel García Márquez', 'Novela', 1967),
    ('1984', 'George Orwell', 'Ciencia Ficción', 1949),
    ('El Quijote', 'Miguel de Cervantes', 'Clásico', 1605),
    ('Crimen y Castigo', 'Fiódor Dostoyevski', 'Novela', 1866),
    ('Harry Potter y la Piedra Filosofal', 'J.K. Rowling', 'Fantasía', 1997),
    ('La Sombra del Viento', 'Carlos Ruiz Zafón', 'Misterio', 2001),
    ('Ficciones', 'Jorge Luis Borges', 'Cuentos', 1944)
]

cursor.executemany('''
INSERT INTO libros (titulo, autor, genero, año_publicacion) VALUES (?, ?, ?, ?)
''', libros)

conexion.commit()
print('✅ Se insertaron los datos de ejemplo correctamente')