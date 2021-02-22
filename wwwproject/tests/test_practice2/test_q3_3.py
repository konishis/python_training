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

from wwwproject.practice2 import q3_3


def test_1():
    q3_3.debtperson.debt = 500000
    q3_3.debtperson.monthrepayament = 10000
    result = q3_3.repaymentyears()
    assert result == 50


def test_2():
    q3_3.debtperson.debt = 500000
    q3_3.debtperson.monthrepayament = 10000
    q3_3.debtperson.bonus = 10000
    result = q3_3.bonusrepaymentboost() // まちがい
    assert result == (500000 / 10000 / 12) - (500000 / 20000 / 12)


def test_3():
    q3_3.debtperson.debt = 500000
    q3_3.debtperson.monthrepayament = 10000
    q3_3.debtperson.targetyear = 2
    result = q3_3.repaymentinbonus()
    assert result == 500000 / 24 - 10000
