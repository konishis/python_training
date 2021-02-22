"""
q3_3【難】

借金返済計画を立てるプログラムを作りたい．
簡単のため，利子は無しとする．
まず，借金の総額と，ひと月に返済する金額を入力すると，
返済にかかる年数を表示し，
さらに，毎年のボーナスから返済する金額を入力すると，
返済完了が何年早まるかを表示し，
その次に返済を完了したい年数を入力すると，
ボーナスからいくら返せばよいかを表示するプログラムを作成せよ．
"""


class debtperson:
    def __init__(self, debt, monthrepayament, bonus, bonusrepayment, targetyear):
        self.debt = debt
        self.monthrepayament = monthrepayament
        self.bonus = bonus
        self.bonusrepayment = bonusrepayment
        self.targetyear = targetyear


def repaymentyears():
    return debtperson.debt / debtperson.monthrepayament


def bonusrepaymentboost():
    return


def repaymentinbonus():
    pass


if __name__ == "__main__":
    debtperson.debt = int(input("借金の総額を入力:"))
    debtperson.monthrepayament = int(input("ひと月に返済する金額:"))
    print("返済にかかる年数:", repaymentyears(), "カ月")
    debtperson.debt = int(input("毎年のボーナスから返済する金額を入力:"))
