class Product:
    def __init__(self, price, description, size):
        self.price = price
        self.description = description
        self.size = size

    def get_price(self):
        return self.price

    def __str__(self) -> str:
        return f'{self.price}, {self.description} {self.size}'
