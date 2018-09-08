from datetime import datetime

from domain.order_type import order_type

class order:
    type: order_type
    id: str
    quantity: int
    price: float
    date: datetime

    def __init__(self, type, id, quantity, price, date):
        self.date = date
        self.price = price
        self.quantity = quantity
        self.id = id
        self.type = type

    def get_sign(self):
        if self.type == order_type.BUY:
            return 1
        return -1

    def get_signed_quantity(self):
        return self.quantity * self.get_sign()

    def get_signed_cash(self):
        return self.quantity * self.get_sign() * self.price * -1



