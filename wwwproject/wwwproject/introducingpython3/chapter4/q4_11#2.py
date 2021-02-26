def makelist():

    list1 = [1, 2, 3]
    print(list1[3])
    print("success")


def errprint():
    print("Err")


def test1():
    try:
        makelist()
    except:
        errprint()


if __name__ == "__main__":
    test1()