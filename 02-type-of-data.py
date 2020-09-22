#!~/.virtualenv/runoob/bin/python
#-*- coding:utf8 -*- 
"""
print('--' * 10)
counter = 100 
miles = 100.0
name = 'runoob'

print('counter:', counter)
print('miles:', miles)
print('name:', name)

print('--' * 10)
a, b, c = 1, 2, 'runoob'
print('a:', a)
print('b:', b)
print('c:', c)
print('--' * 10)

'''
可变数据类型：列表、字典、集合
不可变数据类型：数字、字符串、元组
'''
"""
list_02 = ['abc', '(apple, orange)', 1001, '[1, 2, 3]']

list_01 = ['1024', '2048']

#print(list_01)
#print(list_02[0])
#print(list_02[1][1])
#print(list_02[-1:1])
#print(list_02[2:])
#print(list_02[::-1])
#print(list_02[3:1])
#print(list_02 + list_01[1:])
#print(list_02[1][0])
#print(list_02[1][6])
#
#tuple_01 = (0, 1, 2, 3, 4, 0)
#list_03 = [0, 1, 2, 3, 4, 0]
#set_01 = {"Apple", 'Orange', 'banana', 'Radish', 'Apple'} #只会输出一个Apple，集合具有去重的功能
#
#print(tuple_01)
#print(list_03)
#print(set_01)
#
#tuple_02 = ('[]', '[1024, "cat"]', {'apple', 'Radish'})
#print(tuple_02)
##tuple_02[0][0] = '2048' #元组不可更改

dict_01 = {}
dict_01['1001'] = 'Runoob Object'
dict_01[2] = 'Apple'
print(dict_01['1001'])
print(dict_01[2])
print(dict_01)
print(dict_01.keys())
print(dict_01.values())
