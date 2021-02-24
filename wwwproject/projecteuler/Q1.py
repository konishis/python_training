'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
'''
3 または 5 の倍数である 10 未満のすべての自然な数値をリストすると、
3、5、6、9 が得られます。これらの倍数の合計は 23 です。
1000 以下の 3 または 5 のすべての倍数の合計を検索します。
'''

# def multiplesAnyNum(InAnyNum,Incnt):
#     for num in range(Incnt):
#         if num % InAnyNum == 0:
#             yield num

# def cntmultipleNums(InAnyNum,Incnt):
#     sumnum = 0
#     for count , num in enumerate(multiplesAnyNum(InAnyNum, Incnt),1):
#        sumnum += num
#     return sumnum
 
    
# multipleNum1 = 3
# multipleNum2 = 5
# Count = 1001
# Ans = cntmultipleNums(multipleNum1,Count) + cntmultipleNums(multipleNum2,Count)
# print(Ans)

COUNT = 1000

def sumAnyMultipleNum(InNum):
    tmp = 0
    for num in range(1,COUNT):
        if num % InNum == 0:
            tmp += num
    return tmp

Ans = sumAnyMultipleNum(3) + sumAnyMultipleNum(5)