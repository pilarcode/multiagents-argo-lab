import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session
from multiagents.db.repositories.customer import CustomerRepository 
from multiagents.db.repositories.product import ProductRepository
from multiagents.db.repositories.order import OrderRepository
from multiagents.db.repositories.orderdetail import OrderDetailRepository
from multiagents.db.models import Base, Customer, Product, Order, OrderDetail
from multiagents.config import Configuration
from multiagents.utils import logger 

log = logger.get_logger(__name__)


# Función para crear la base de datos
def get_database(db_url:str):
    """ Create the database if it doesn't exist. 
    Args:
        db_url (str): url of the database
    Returns:
        engine: Engine of the database
    """
    try:
        # Crear la conexión al motor de la base de datos
        engine = create_engine(db_url, echo=True)
        log.info("Conexión a la base de datos establecida.")

        # Crear todas las tablas definidas en las clases
        Base.metadata.create_all(engine)
        log.info("Base de datos creada exitosamente.")
        return engine
    except SQLAlchemyError as e:
        log.error(f"Error al crear la base de datos: {e}")
        raise ValueError(f"Error al crear la base de datos.{e}")

def create_session(engine)-> Session:
    """ Create a session to interact with the database.
    Args:
        engine: Engine of the database
    Returns:
        session: Session of the database
    """
    log.info("Creando la sesión de la base de datos.")
    Session = sessionmaker(bind=engine,autocommit=False, autoflush=False)
    session = Session()
    return session

def load_csv_to_dataframe(csv_file_path: str) -> pd.DataFrame:
    """Carga un archivo CSV en un DataFrame."""
    try:
        df = pd.read_csv(csv_file_path, sep=',')
        log.info(f"Archivo CSV {csv_file_path} cargado correctamente.")
        return df
    except Exception as e:
        log.error(f"Error al cargar el archivo CSV {csv_file_path}: {e}")
        raise

def init_customers(db: Session, csv_file_path:str):
    """ Initialize a table from a CSV file."""
    
    table_name = "Customers"
    log.info(f"Initializing table {table_name} from {csv_file_path}")

    # Open the CSV file
    df = load_csv_to_dataframe(csv_file_path)

    # Iterate over the rows and insert them into the table
    for index, row in df.iterrows():
        
        first_name = row['FirstName']
        last_name = row['LastName']
        email = row['Email']
        phone = row['Phone']
        address = row['Address']
        # Insert the row into the table
        CustomerRepository.create_customer(db, first_name, last_name, email, phone, address)

        log.info(f"Customer created successfully. {row}")
    log.info(f"Table {table_name} initialized successfully.")

def init_products(db: Session, csv_file_path:str):
    """ Initialize a table from a CSV file."""
    
    table_name = "Products"
    log.info(f"Initializing table {table_name} from {csv_file_path}")

    # Open the CSV file
    df = load_csv_to_dataframe(csv_file_path)
    
    # Iterate over the rows and insert them into the table
    for index, row in df.iterrows():
        name = row['Name']
        description = row['Description']
        price = row['Price']
        stock_quantity = row['StockQuantity']
        category = row['Category']
        # Insert the row into the table
        ProductRepository.create_product(db, name, description, price, stock_quantity, category)

        log.info(f"Customer created successfully. {row}")
    log.info(f"Table {table_name} initialized successfully.")

def init_orders(db: Session, csv_file_path:str):
    """ Initialize a table from a CSV file."""
    
    table_name = "Orders"
    log.info(f"Initializing table {table_name} from {csv_file_path}")

    # Open the CSV file
    df = load_csv_to_dataframe(csv_file_path)

    # Iterate over the rows and insert them into the table
    for index, row in df.iterrows():
        customer_id = row['CustomerID']
        order_date = row['OrderDate']
        total_amount = row['TotalAmount']
        # Insert the row into the table
        OrderRepository.create_order(db, customer_id, order_date,total_amount)

        log.info(f"Customer created successfully. {row}")
    log.info(f"Table {table_name} initialized successfully.")

def init_orderdetails(db: Session, csv_file_path:str):
    """ Initialize a table from a CSV file."""
    
    table_name ='OrderDetails'
    log.info(f"Initializing table {table_name} from {csv_file_path}")

    # Open the CSV file
    df = load_csv_to_dataframe(csv_file_path)

    # Iterate over the rows and insert them into the table
    for index, row in df.iterrows():
        order_id = row['OrderID']
        product_id = row['ProductID']
        quantity = row['Quantity']
        subtotal = row['Subtotal']
        # Insert the row into the table
        OrderDetailRepository.create_order_detail(db, order_id, product_id, quantity, subtotal)

        log.info(f"Customer created successfully. {row}")
    log.info(f"Table {table_name} initialized successfully.")


def init_database():
    """ Initialize the database with some data.
    Args:
        config (Configuration): Configuration object
    Returns:
        session: Session of the database
    """
 
    config = Configuration()
    log.info("Creando y conectando a la base de datos.")

    db_path = config.database_path
  
    if os.path.exists(db_path):
        os.remove(db_path)
        log.info("Base de datos eliminada.")
    engine = get_database(db_url=config.database_url)

    log.info("Creando la sesión de la base de datos.")
    session = create_session(engine)

    log.info("Añadiendo datos a la base de datos.")
    init_customers(session,config.customers_csv_path )
    init_products(session, config.products_csv_path) 
    init_orders(session,config.orders_csv_path)
    init_orderdetails(session,config.order_details_csv_path)

    return session
