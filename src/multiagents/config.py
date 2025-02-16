import os
from dotenv import find_dotenv, load_dotenv

class Configuration:
    """ Configuration class for the application. """
    def __init__(self):
        # Load environment variables
        _ = load_dotenv(find_dotenv())
        self.database_path = os.getenv("DATABASE_PATH")
        self.database_url =  db_url = f"sqlite:///{self.database_path}"
        self.customers_csv_path = os.getenv("CUSTOMERS_CSV_PATH")
        self.products_csv_path = os.getenv("PRODUCTS_CSV_PATH")
        self.orders_csv_path = os.getenv("ORDERS_CSV_PATH")
        self.order_details_csv_path = os.getenv("ORDER_DETAILS_CSV_PATH")
    
    


      