import requests
import os


class FileHandler:
    __file_name = 'buffer.json'

    def __init__(self, file_name):
        self.__file_name = file_name
        try:
            self.read()
        except FileNotFoundError:
            with open(self.__file_name, 'w') as f:
                self.write('')

    def write(self, data):
        with open(self.__file_name, 'w') as f:
            f.write(str(data))
            print("data written to file")

    def read(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as f:
                data = f.read()
                return data
        except FileNotFoundError:
            return 'File not found'


'''  def set_data(self, data:list):
      """data = api.Request().get()"""
      if data[1] == 200:
          return data[0]
      else:
          return None'''

file_buffer = FileHandler("buffer.json")
file_currency = FileHandler("currencies.json")
