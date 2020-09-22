#-*- coding:utf-8 -*-

#实例1
total = 0
list1 = [11, 12, 13, 14, 15]
for ele in range(0, len(list1)):
    total = total + list1[ele]

print("列表元素之和:", total)

#实例2 使用while循环
total = 0
ele = 0
list1 = [11, 12, 13, 14, 15]
while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1
print("列表元素之和:", total)

#使用递归
list1 = [11, 12, 14, 15, 13]

def sumOfList(list, size):
    if(size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

total = sumOfList(list1, len(list1))
print("列表元素之和:", total)
