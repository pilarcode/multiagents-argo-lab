from sqlalchemy.orm import Session
from multiagents.db.models import Order
from multiagents.utils import logger 
from datetime import datetime

log = logger.get_logger(__name__)

class OrderRepository:
    """ Repository for order operations """
    @staticmethod
    def create_order(db: Session, customer_id: int, str_order_date:str, total_amount: float):
        """
        Creates a new order record in the database.

        Args:
            db (Session): The database session used for the transaction.
            customer_id (int): The ID of the customer.
            order_date (datetime.date): The date when the order was placed.
            total_amount (float): The total cost of the order.

        Returns:
            Order: The newly created Order object.
        """
        # Convert the string to a date object
        order_date = datetime.strptime(str_order_date, '%Y-%m-%d').date()

        db_order = Order(CustomerID=customer_id, OrderDate=order_date, TotalAmount=total_amount)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
