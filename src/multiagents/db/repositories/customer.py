from sqlalchemy.orm import Session
from multiagents.db.models import Customer
from multiagents.utils import logger 

log = logger.get_logger(__name__)


class CustomerRepository:
    """ Repository for customer operations """
    @staticmethod
    def create_customer(db: Session, first_name, last_name, email, phone=None, address=None):
        """
        Creates a new customer record in the database.

        Args:
            db (Session): The database session used for the transaction.
            first_name (str): The first name of the customer.
            last_name (str): The last name of the customer.
            email (str): The email address of the customer.
            phone (str, optional): The phone number of the customer. Defaults to None.
            address (str, optional): The address of the customer. Defaults to None.

        Returns:
            Customer: The newly created Customer object.
        """
        db_customer = Customer(FirstName=first_name, LastName=last_name, Email=email, Phone=phone, Address=address)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        log.info("Customer created successfully")
        return db_customer

    @staticmethod
    def get_customer_by_id(db: Session, customer_id: int):
        """Get a customer by their ID.

        Args:
            db (Session): The database session used for the transaction.
            customer_id (int): The ID of the customer to retrieve.

        Returns:
            Customer: The Customer object if found, otherwise None."""
        log.info(f"Getting customer with id: {customer_id}")
        return db.query(Customer).filter(Customer.customer_id == customer_id).first()

