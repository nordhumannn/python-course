class Customer:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number  = phone_number

    def __str__(self) -> str:
        return f'{self.name}, {self.surname}, {self.phone_number}'
