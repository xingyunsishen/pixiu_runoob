#-*- coding:utf8 -*-

num = float(input("please input a number:"))
'''
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")
'''
#if内嵌
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")

