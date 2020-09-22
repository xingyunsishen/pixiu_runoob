#-*- coding: utf-8 -*-
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum

#调用函数
n = int(input('大佬：要计算多少个数:'))
print(sumOfSeries(n))

