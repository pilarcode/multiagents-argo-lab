import sqlite3
from sqlite3 import Connection

def get_db_connection() -> Connection:
    """Crea y retorna una conexión a la base de datos SQLite."""
    connection = sqlite3.connect('database.db')  # Ajusta el nombre de la base de datos si es necesario
    connection.row_factory = sqlite3.Row  # Para permitir acceso por nombre de columna
    return connection
