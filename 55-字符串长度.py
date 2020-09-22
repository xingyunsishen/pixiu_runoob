#-*- coding:utf-8 -*-
#len函数
str = "runoob"
print(len(str))

#使用循环计算
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
str = "runoob"
print(findLen(str))
