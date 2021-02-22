"""for vs comprehensions
    speed check"""

import timeit


def forloop():
    """0-10000までのリスト作成"""
    extension_1 = []
    for i in range(10000):
        extension_1.append(i)
    return extension_1


def comprehensions():
    """0-10000までのリスト作成"""
    comprehension_1 = [i for i in range(10000) if i % 2 == 0]
    # comprehension_1 = list(range(10000))

    return comprehension_1


result = timeit.timeit("forloop()", globals=globals(), number=1000)
print("forloop result:       ", result / 1000)

result = timeit.timeit("comprehensions()", globals=globals(), number=1000)
print("comprehensions result:", result / 1000)
