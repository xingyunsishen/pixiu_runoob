#-*- coding:utf8 -*-

import cmath

a = float(input("please input a:"))
b = float(input("please input b:"))
c = float(input("please input c:"))

#计算
d = (b ** 2) - (4 * a * c)

#两种方法
sol1 = (-b - cmath.sqrt(d))/(2 * a)
sol2 = (-b + cmath.sqrt(d))/(2 * a)

print("结果为:{0}和{1}".format(sol1, sol2))

