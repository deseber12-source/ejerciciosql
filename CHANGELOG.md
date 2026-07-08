Todos los cambios de conforme vaya avanzado el proyecto se iran registrando aqui

## [0.0.1] - 2026-07-07

### Agregado: 

- Se creo CHANGELOG y README
- Se añadio una pequeña calculadora para entrenar commits y ver historial en la consola

## [0.0.2] - 2026-07-07

### Agregado: 
- .gitignore

## [0.0.3] - 2026-07-07

### modificacion:

- Se creo base de datos desde python con sqlite3 en el archivo **base.py** se ignora con .gitignore
- Se declaro la variable **cursor = conexion.cursor()** para usarla en el resto del archivo
- Se agregaron unas tablas para simular una libreria, donde existen usuarios, libros y prestamos de libros, aqui se relaciona con usuarios_id y libro_id, entonces se ocupo, por ejemplo FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id).
- cuando se finalizo, se uso **conexion.commit()**
- SE AGREGARON datos de ejemplo en el archivo. Para agregarlos a sqlite, despues de los datos simulados, se ejecuto **cursor.executemany(''' INSERT INTO name_tabla (llave1, llave2, llave 3) VALUES (?, ?, ?) ''')**
- depsues se agrego de nuevo un **conexion.coomit()** y desppues un print para confirmar la base de datos-

