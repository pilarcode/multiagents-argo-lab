import os
from sqlalchemy import create_engine, text
from lab.utils import logger

log = logger.get_logger(__name__)

def execute_script_sql(engine, script_sql):
    """ Ejecutar un script SQL en una base de datos SQLite. 
    
    Args:
        engine (sqlalchemy.engine.Engine): Motor de base de datos.
        script_sql (str): Ruta del archivo SQL a ejecutar.
    """
    # Leer el archivo SQL y ejecutarlo
    with open(script_sql, 'r') as file:
        sql = file.read()
    
    # Usar el engine para ejecutar el script SQL
    with engine.connect() as connection:
        connection.execute(text(sql))

    log.info(f"Script {script_sql} ejecutado correctamente.")

def database_exists(db_path: str) -> bool:
    """ Comprobar si la base de datos SQLite ya existe. 
    
    Args:
        db_path (str): Ruta al archivo de la base de datos.
    
    Returns:
        bool: True si la base de datos existe, False si no.
    """
    
    return os.path.exists(db_path)


def create_database(schema_sql_path:str, data_sql_path:str, db_path:str):
    """ Crear la base de datos y cargar los datos iniciales. 
    
    Args:
        schema_sql_path (str): Ruta del archivo SQL que contiene el esquema de la base de datos.
        data_sql_path (str): Ruta del archivo SQL que contiene los datos iniciales.
    """
    
    # Crear el motor de base de datos (en este caso SQLite)
    engine = create_engine(f"sqlite:///{db_path}", echo=True)

    try:
        log.info("Iniciando la creación de la base de datos...")
        # Ejecutar el script para crear el esquema
        execute_script_sql(engine, schema_sql_path)

        log.info("Esquema de la base de datos creado correctamente.")

        # Ejecutar el script para insertar los datos
        #execute_script_sql(engine, data_sql_path)

        #log.info("Datos iniciales creados correctamente.")
    
    except Exception as e:
        log.error(f"Error al crear la base de datos: {e}")



if __name__ == "__main__":


    create_database(schema_sql_path="app/scripts/schema.sql", data_sql_path="../../app/scripts/init_data.sql", db_path="shop.db")