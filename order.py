class Order:
    def __init__(self, customer, *products):
        self.customer_name = f'{customer.name} {customer.surname}'
        self.contact = customer.phone_number
        self.products = products

    def total_price(self):
        total = 0
        for i in self.products:
            total += i.get_price()
        return total

    def order_list(self):
        order_list = ''
        count = 1
        for item in self.products:
            order_list += f'{count}) {item}\n'
            count += 1
        return order_list

    def __str__(self) -> str:
        return f'----- Order -----\n\nCustomer: {self.customer_name}\nContact: {self.contact}\nItems: {Order.order_list(self)} \nTotal price: {Order.total_price(self)}$'
