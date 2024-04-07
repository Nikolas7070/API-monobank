from api import Request
from filehandler import FileHandler


class Main:
    def get_price(self, price):
        return Request().enter_field(price)

    def convertor(self, uah, value):
        return Request().converter(uah, value)


print(Main().convertor(50, 'USD'))
