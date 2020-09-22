#-*- coding:utf-8 -*-
list1 = [10, 11, 12, 14, 13]
list1.sort()
print("最小元素为:", *list1[:1])
print("最大元素为:", list1[-1])
print("最小元素为:", min(list1))
print("最大元素为:", max(list1))


