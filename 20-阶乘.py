#-*- coding:utf-8 -*-
#接收用户输入
num = int(input('please input a number:'))
factorial = 1

#判断数字是负数、0or正数
if num < 0:
    print("抱歉，负数没有阶乘")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("{0}的阶乘是{1}".format(num, factorial))
