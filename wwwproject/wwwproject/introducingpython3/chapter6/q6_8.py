class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return "name:%s, symbol:%s, number:%s" % (self.name, self.symbol, self.number)


hydrodict = {"name": "hydrogen", "symbol": "H", "number": 1}

hydroobject = Element(**hydrodict)
print(hydroobject)

print(hydroobject.name)