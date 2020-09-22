#-*- coding:utf-8 -*-
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [8, 0, 8, 20, 10, 0, 3, 4, 5, 6, 4, 8]
x = 8
print(countX(lst, x))

#使用count()方法
def countX(lst, x):
    return lst.count(x)

lst = [8, 2, 3, 4, 4, 5, 6, 1, 2, 8]
x = int(input("请输入0-9数字:"))
print(countX(lst, x))
