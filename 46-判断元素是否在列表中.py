#-*- coding:utf-8 -*-
test_list = [1, 4, 5, 6, 7, 13, 10]
print("查看4是否在列表中(使用循环):")
for i in test_list:
    if(i == 4):
        print("不存在")
print("查看4是否在列表中(使用in关键字):")

if(4 in test_list):
    print("存在")

from bisect import bisect_left

#初始化列表
test_list_set = [1, 4, 5, 3, 6, 7]
test_list_bisect = [1, 2, 4, 8, 10]

print("查看4是否在列表中(使用set() + in):")

test_list_set = set(test_list_set)
if 4 in test_list_set:
    print("存在")

print("查看4是否在列表中(使用sort() + bisect_left()):")

test_list_bisect.sort()
if bisect_left(test_list_bisect, 4):
    print("存在")
