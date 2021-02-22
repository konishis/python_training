from wwwproject.practice1 import q1_randomlist


def test_1():
    result = q1_randomlist.createrandlist(10)
    assert len(result) == 10


def test_2():
    result = q1_randomlist.createrandlist(5)
    assert len(result) == 5


def test_3():
    result = q1_randomlist.createrandlist(3)
    assert len(result) == 3
