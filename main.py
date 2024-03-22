import requests
import os

import api


class FileHandler:
    def __init__(self):
        with open('buffer.json', 'r') as f:
            data = f.read()
            if data == '':
                with open('buffer.json', 'w') as f:
                    f.write(api.Request().get())


FileHandler()
