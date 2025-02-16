from sqlalchemy.orm import Session
from multiagents.db.models import OrderDetail
from multiagents.utils import logger 

log = logger.get_logger(__name__)


class OrderDetailRepository:
    """ Repository for order detail operations """
    @staticmethod
    def create_order_detail(db: Session, order_id, product_id, quantity, subtotal):
        """
        Creates a new order detail record in the database.

        Args:
            db (Session): The database session used for the transaction.
            order_id (int): The ID of the order.
            product_id (int): The ID of the product.
            quantity (int): The quantity of the product.
            subtotal (float): The subtotal of the order detail.

        Returns:
            OrderDetail: The newly created OrderDetail object.
        """
        db_order_detail = OrderDetail(OrderID=order_id, ProductID=product_id, Quantity=quantity, Subtotal=subtotal)
        db.add(db_order_detail)
        db.commit()
        db.refresh(db_order_detail)
        return db_order_detail
