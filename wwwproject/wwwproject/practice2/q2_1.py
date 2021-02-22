"""q2_1"""


def calculate(case):
    """calculate result"""
    if case == 1:
        result = (33 + 44) * 55
        print("(33+44)*55=", result)
        return result
    elif case == 2:
        result = 2.1 + 4.3 + 6.5
        print("2.1+4.3+6.5=", result)
        return result
    else:
        result = (123 + 456) % 78
        print("(123+456)%78=", result)
        return result
