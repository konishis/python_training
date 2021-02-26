class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("name:%s, symbol:%s, number:%s" % (self.name, self.symbol, self.number))


hydrodict = {"name": "hydrogen", "symbol": "H", "number": 1}

hydroobject = Element(**hydrodict)
hydroobject.dump()