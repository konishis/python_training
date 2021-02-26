class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


temp = Element("Hydrogen", "H", 1)
print(temp.name)