from filehandler import file_currency

class CurrenciesConvertor:
    def iso_to_name(self, iso_code):
        file = eval(file_currency.read())
        for x in file:
            res = file[x]['ISOnum']
            if res == iso_code:
                return x


print(CurrenciesConvertor().iso_to_name(784))


