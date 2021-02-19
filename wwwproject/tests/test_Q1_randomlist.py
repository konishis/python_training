from wwwproject import Q1_randomlist


def test_1():
    result = Q1_randomlist.createrandlist(10)
    assert len(result) == 10


def test_2():
    result = Q1_randomlist.createrandlist(5)
    assert len(result) == 5


def test_3():
    result = Q1_randomlist.createrandlist(3)
    assert len(result) == 3
