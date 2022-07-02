from person import Person

class Student(Person):

    def __init__(self, name: str, surname: str, age: int, country: str):
        super().__init__(age, country)
        self.name = name.strip().title()
        self.surname = surname.strip().title()

    def __str__(self):
        return f'{self.name} {self.surname}, {super().__str__()}'
