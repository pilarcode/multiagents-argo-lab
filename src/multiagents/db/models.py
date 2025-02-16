
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Customer(Base):
    """ Customer model that represents the customers """
    __tablename__ = 'Customers'
    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Email = Column(String, unique=True, nullable=False)
    Phone = Column(String)
    Address = Column(String)

    orders = relationship('Order', back_populates='customer')

    
class Product(Base):
    """ Product model that represents the products """
    __tablename__ = 'Products'
    ProductID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Description = Column(String)
    Price = Column(Float, nullable=False)
    StockQuantity = Column(Integer, nullable=False)
    Category = Column(String, nullable=False)

    order_details = relationship('OrderDetail', back_populates='product')

    
class Order(Base):
    """ Order model that represents the orders """
    __tablename__ = 'Orders'
    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'), nullable=False)
    OrderDate = Column(Date, nullable=False)
    TotalAmount = Column(Float, nullable=False)

    customer = relationship('Customer', back_populates='orders')
    order_details = relationship('OrderDetail', back_populates='order')


class OrderDetail(Base):
    """ OrderDetail model  that represents the order details """
    __tablename__ = 'OrderDetails'
    OrderDetailID = Column(Integer, primary_key=True, autoincrement=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'), nullable=False)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Subtotal = Column(Float, nullable=False)

    order = relationship('Order', back_populates='order_details')
    product = relationship('Product', back_populates='order_details')
