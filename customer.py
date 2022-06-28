class Customer:
    
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number  = phone_number

    def __str__(self) -> str:
        return f'{self.name} - {self.phone_number}'
