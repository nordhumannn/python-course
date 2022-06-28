class Product:
    
    def __init__(self, price: int | float, description: str):
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f'{self.description} - {self.price}'
