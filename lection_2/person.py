class Person:

    def __init__(self, age: int, country: str):
        self.age = age
        self.country = country

    def __str__(self):
        return f'{self.age}, {self.country}'
