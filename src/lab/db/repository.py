from lab.db.models import Customer, Product, Order, OrderDetail

class CustomerRepository:
    @staticmethod
    def create_customer(first_name, last_name, email, phone=None, address=None):
        Customer.create(first_name, last_name, email, phone, address)

    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.get_by_id(customer_id)

# Implementar repositorios para los productos, pedidos y detalles de pedidos
