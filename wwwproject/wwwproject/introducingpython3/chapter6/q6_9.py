class bear:
    def eats(self):
        return "berries"


class Rabbit:
    def eats(self):
        return "clover"


class Octothorpe:
    def eats(self):
        return "campers"


pusan = bear()
rabbit = Rabbit()
sharp = Octothorpe()

print(pusan.eats())
print(rabbit.eats())
print(sharp.eats())
