from sqlalchemy.orm import Session
from multiagents.db.models import Product
from multiagents.utils import logger 

log = logger.get_logger(__name__)


class ProductRepository:
    """ Repository for product operations """
    @staticmethod
    def create_product(db: Session, name, description, price, stock_quantity, category):  
        """
        Creates a new product record in the database.

        Args:
            db (Session): The database session used for the transaction.
            name (str): The name of the product.
            description (str): The description of the product.
            price (float): The price of the product.
            stock_quantity (int): The stock quantity of the product.
            category (str): The category of the product.

        Returns:
            Product: The newly created Product object.
        """

        db_product = Product(Name=name, Description=description, Price=price, StockQuantity=stock_quantity, Category=category)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        log.info("Product created successfully")
        return db_product

    @staticmethod
    def get_product_by_id(db: Session, product_id: int):
        """
        Retrieves a product by its ID.

        Args:
            db (Session): The database session used for the transaction.
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The Product object if found, otherwise None.
        """
        log.info(f"Getting product with id: {product_id}")
        return db.query(Product).filter(Product.product_id == product_id).first()
