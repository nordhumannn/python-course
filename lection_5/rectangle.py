import math

class NegativeValue(Exception):
    
    def __init__(self, message):
        super().__init__()
        self.message = message

class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        if width <= 0 or height <= 0:
            raise NegativeValue('Positive numbers only')
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()
    
    def __add__(self, other):
        return Rectangle(1, self.get_area() + other.get_area())

    def __mul__(self, other):
        return Rectangle(self.width * math.sqrt(other), self.height * math.sqrt(other))

    def __str__(self) -> str:
        return f'W: {self.width}, L: {self.height}, Area: {self.get_area()}'

rec_1 = Rectangle(2, 8)
rec_2 = Rectangle(2, 4)
rec_3 = Rectangle(7, 9)

# print(rec_1 < rec_2)
# print(rec_1 > rec_2)
print(rec_1 + rec_2)
# print(rec_2 * 100)
