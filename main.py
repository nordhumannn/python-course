from product import Product
from customer import Customer
from order import Order

pr_1 = Product(20, 'Apple')
pr_2 = Product(30, 'Banana')

cust_1 = Customer('Andrew', '+1234567890')
cust_2 = Customer('John', '+0987654321')

order_1 = Order(cust_1)
order_2 = Order(cust_2)

order_1.add_product(pr_1, 2)
order_1.add_product(pr_2, 2)
order_1.add_product(pr_1, 1)

order_2.add_product(pr_1, 3)

print(order_1)
