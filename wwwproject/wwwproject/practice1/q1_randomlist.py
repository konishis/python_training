"""
This file is python training
http://coze.s201.xrea.com/python/prac.html
"""

import random


def createrandlist(listsize):
    """0-100までのランダムな値をlistsize個生成し、リストで返す"""
    return [random.randint(0, 100) for i in range(listsize)]
