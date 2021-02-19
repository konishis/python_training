import random


def createrandlist(listsize):
    return [random.randint(0, 100) for i in range(listsize)]
