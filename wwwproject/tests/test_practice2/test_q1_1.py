from wwwproject.practice2 import q1_1


def test_1():
    result = q1_1.hello()
    assert result == "Hello World"


def test_2():
    result = q1_1.calculate()
    assert result == 24