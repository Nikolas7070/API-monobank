import requests


class Request:
    def __init__(self):
        self.data = requests.get(f"https://api.monobank.ua/bank/currency").text

    def get(self):
        return str(self.data)


