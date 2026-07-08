import sqlite3

def conectar():
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()
    return conexion, cursor
