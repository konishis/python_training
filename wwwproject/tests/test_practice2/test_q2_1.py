from wwwproject.practice2 import q2_1


def test_1():
    result = q2_1.calculate(1)
    assert result == 4235


def test_2():
    result = q2_1.calculate(2)
    assert result == 12.9


def test_3():
    result = q2_1.calculate(3)
    assert result == 33