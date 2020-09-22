#-*- coding:utf8 -*-
import math


num01 = input("请输入第一个数字：")
num02 = input('请输入第二个数字：')
#判断是否是数字
if num01.isdigit() and num02.isdigit():
    print('两次输入均为数字')
    num01 = int(num01)
    num02 = int(num02)
    #求和
    sum = num01 + num02
    print('sum=', sum)
    
    #求差
    difference = num01 - num02
    print('difference=', difference)
    
    #求积
    quadrature = num01 * num02
    print('quadrature=', quadrature)
    
    #求商
    division = num01 / num02
    print('division=', division)
    
    #取整除
    divide = num01 // num02
    print('divide=', divide)
    
    #取模
    modulo = num01 % num02
    print('modulo=', modulo)
    
    #取绝对值
    abs_value = abs(num01 - num02)
    print('abs_value=', abs_value)
else:
    print("请重新输入")
#
print('over')
