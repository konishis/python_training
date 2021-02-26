class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrodict = {"name": "hydrogen", "symbol": "H", "number": 1}

hydroobject = Element(**hydrodict)
print(hydroobject.number)