import requests
from filehandler import file_buffer, file_currency


class Request:
    def __init__(self):
        self.data = requests.get(f"https://api.monobank.ua/bank/currency")

    def set(self):
        return file_buffer.read()

    def get(self):
        if self.data.status_code == 200:
            file_buffer.write(self.data.text)
            return self.data.text, self.data.status_code

    def delete(self):
        empty_data = '[]'
        file_buffer.write(empty_data)
        return True

    def get_currency(self, currency_code):
        self.get()
        data = eval(self.set())
        for currency_data in data:
            if 'currencyCodeA' in currency_data and 'currencyCodeB' in currency_data:
                if currency_data['currencyCodeA'] == currency_code:
                    currency_code_A = currency_data['currencyCodeA']
                    currency_code_B = currency_data['currencyCodeB']
                    print(currency_code_A, currency_code_B)
                    break

    def name_to_iso(self, currency_name):
        file = eval(file_currency.read())
        for x in file:
            res = file[x]
            if x == currency_name:
                return res['ISOnum']

    def iso_to_buffer(self, ISOnum):
        file = eval(file_buffer.read())
        for x in file:
            if ISOnum == x['currencyCodeA']:
                return x

    def enter_field(self, name):
        iso_num = self.name_to_iso(name)
        if iso_num:
            res = self.iso_to_buffer(iso_num)
            try:
                return res["rateBuy"]
            except KeyError:
                return res['rateCross']

    def converter(self, uah, value):
        rate = self.enter_field(value)
        if rate:
             return round(uah / rate, 2)
        else:
            return None



