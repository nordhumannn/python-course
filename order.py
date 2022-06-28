from product import Product
from customer import Customer

class Order:
    
    def __init__(self, customer: Customer):
        self.customer = customer
        self.cart = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        self.cart.append(product)
        self.quantities.append(quantity)


    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantities[i]
        return total

    def __str__(self):
        res = f'Customer: {self.customer}\n'

        for i, item in enumerate(self.cart):
            tmp = f'\t{item} UAH * {self.quantities[i]} = {self.quantities[i] * item.price}\n'
            res += tmp

        res += f'\nTotal price: {self.total_price()} UAH'

        return res
