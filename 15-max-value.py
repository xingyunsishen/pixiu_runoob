#-*- coding:utf8 -*-

a = input('please input a:')
b = input('please input b:')

#使用max函数,可以对字符或者数字进行取值
res = max(a, b)
print("{0}是最大值".format(res))

#max还可以对列表和元组使用
list_01 = []

i = 0
while i <= 5:
    list_01.append(i)
    i = i + 1
'''
list_01 = [1, 2]
print(list_01)
list_01.append(3)
print(list_01)
res = max(list_01)
'''
print(list_01)
res = max(list_01)
print("{0}是最大值".format(res))

tuple_01 = (11, 22)
res = max(tuple_01)
print('{0}是最大值'.format(res))
