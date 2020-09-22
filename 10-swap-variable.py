#-*- coding:utf8 -*-
x = input("please input x:")
y = input("please input y:")
#创建临时变量temp
temp = x
x = y
y = temp

print("交换后x的值:{}".format(x))
print("交换后y的值:{}".format(y))
#第二种方法，python中最简单的方式

x, y = y, x
print("交换后x的值:%s, y的值:%s" %(x, y))
