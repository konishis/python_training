"""
This file is python training
http://coze.s201.xrea.com/python/prac.html
"""

import random


def createrandlist(listsize, lower=0, upper=100):
    """lower-upperまでのランダムな値をlistsize個生成し、リストで返す"""
    return [random.randint(lower, upper) for i in range(listsize)]


if __name__ == "__main__":
    print(createrandlist(10, 2, 3))
