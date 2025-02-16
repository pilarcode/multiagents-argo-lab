from lab.db.database import get_db_connection

class Customer:
    """ Represents a customer in the database."""
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def create(first_name, last_name, email, phone=None, address=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
            VALUES (?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, address))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(customer_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers WHERE CustomerID = ?', (customer_id,))
        customer_data = cursor.fetchone()
        conn.close()
        if customer_data:
            return Customer(**customer_data)
        return None

class Product:
    def __init__(self, product_id=None, name=None, description=None, price=None, stock_quantity=None, category=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity
        self.category = category

    @staticmethod
    def create(name, description, price, stock_quantity, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Products (Name, Description, Price, StockQuantity, Category)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, description, price, stock_quantity, category))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products WHERE ProductID = ?', (product_id,))
        product_data = cursor.fetchone()
        conn.close()
        if product_data:
            return Product(**product_data)
        return None

class Order:
    def __init__(self, order_id=None, customer_id=None, order_date=None, total_amount=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount

    @staticmethod
    def create(customer_id, order_date, total_amount):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
            VALUES (?, ?, ?)
        ''', (customer_id, order_date, total_amount))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Orders WHERE OrderID = ?', (order_id,))
        order_data = cursor.fetchone()
        conn.close()
        if order_data:
            return Order(**order_data)
        return None

class OrderDetail:
    def __init__(self, order_detail_id=None, order_id=None, product_id=None, quantity=None, subtotal=None):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.subtotal = subtotal

    @staticmethod
    def create(order_id, product_id, quantity, subtotal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal)
            VALUES (?, ?, ?, ?)
        ''', (order_id, product_id, quantity, subtotal))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_order_id(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM OrderDetails WHERE OrderID = ?', (order_id,))
        order_details_data = cursor.fetchall()
        conn.close()
        return [OrderDetail(**row) for row in order_details_data]
