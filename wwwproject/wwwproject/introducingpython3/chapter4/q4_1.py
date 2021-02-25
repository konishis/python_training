"""7と比較"""


def sevencheck(checknum):
    """
    戻り値
    0:7と等しい場合
    1:7より小さい場合
    2:7より大きい場合
    """
    if checknum == 7:
        print("just right")
        return 0
    if checknum < 7:
        print("too low")
        return 1
    print("too high")
    return 2
