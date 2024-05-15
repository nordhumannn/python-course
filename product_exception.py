class NegativeValue(Exception):
    
    def __init__(self, value: int | float=None, msg: str=None):
        super().__init__()
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'{self.value}, {self.msg}'

class Product:
    
    def __init__(self, price: int | float, description: str):

        if not isinstance(price, (int, float)):
            raise TypeError()

        if price <= 0:
            raise NegativeValue(price, 'price attribute must be positive')

        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f'{self.description} - {self.price}'
