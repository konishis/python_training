"""
戻り値
0:7と等しい場合
1:7より小さい場合
2:7より大きい場合

"""

from wwwproject.introducingpython3.chapter4 import q4_1


def test_1():
    result = q4_1.sevencheck(7)
    assert result == 0


def test_2():
    result = q4_1.sevencheck(6)
    assert result == 1


def test_3():
    result = q4_1.sevencheck(8)
    assert result == 2