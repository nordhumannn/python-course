from product import Product
from customer import Customer
from order import Order

product_1 = Product(199, 'XboX gamepad', '15x20')
product_2 = Product(350, 'Keyboard', '40X20')

customer_1 = Customer('John', 'Doe', '+2948239842')

order_1 = Order(customer_1, product_1, product_2)

print(order_1)
