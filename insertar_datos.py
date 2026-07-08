from database import conectar

conexion, cursor = conectar()

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
conexion.close()