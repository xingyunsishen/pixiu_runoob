#-*- coding:utf-8 -*-
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1, 2, 3, 4]
list2 = [12, 3, 4, 5]
print(multiplyList(list1))
print(multiplyList(list2))
