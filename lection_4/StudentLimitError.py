class StudentLimitError(Exception):
    
    def __init__(self, value: int | float=None, msg: str=None):
        super().__init__()
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'{self.value}, {self.msg}'
