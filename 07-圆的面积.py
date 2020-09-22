#-*- coding:utf-8 -*-

import cmath

r = float(input("请输入半径r:"))

#定义一个方法计算圆的面积
def findArea(r):
    Pi = 3.142
    return Pi * (pow(r, 2))

#调用方法
print("圆的面积:%.6f" %findArea(r))
