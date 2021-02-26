class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.Laser = Laser()
        self.Claw = Claw()
        self.SmartPhone = SmartPhone()

    def does(self):
        return """
%s の有する能力
My Laser : %s
My Claw : %s
My SmartPhone : %s
""" % (
            __class__.__name__,
            self.Laser.does(),
            self.Claw.does(),
            self.SmartPhone.does(),
        )


michel = Robot()

print(michel.does())
