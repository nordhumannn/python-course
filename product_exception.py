class NegativeValue(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def return_exception(self):
        return self.msg

class Product:
    
    def __init__(self, price: int | float, description: str):
        super().__init__()
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f'{self.description} - {self.price}'

while True:
    try:
        price = float(input("Input price: "))
        if price < 0:
            raise NegativeValue("Price can't be negative, please input positive number")
        break
    except ValueError:
        print("ValueError: Only integers acceptable")
    except NegativeValue as err:
        print(err.return_exception())

pr_1 = Product(price, 'Apple')
print(pr_1)
