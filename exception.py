class NegativeValue(Exception):

    def __init__(self, msg):
        self.msg = msg

    def return_exception(self):
        return self.msg

while True:
    try:
        price = float(input("Input price: "))
        if price < 0:
            raise NegativeValue("Price can't be negative, please input positive number")
        break
    except ValueError as error:
        print("Integers only\n", error)
    except NegativeValue as error:
            print(error.return_exception())
