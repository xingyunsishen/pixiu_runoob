#-*- coding:utf8 -*-
import cmath
num = float(input('please input a number:'))

num_sqrt = num ** 0.5  #此方法只适用于num01是正数的时候
print("%0.3f的平方根为%0.3f" %(num, num_sqrt))

num = int(input('please enter a number:'))
num_sqrt = cmath.sqrt(num) 
print('{0}的平方根为{1:0.3f}+{2:0.3f}'.format(num, num_sqrt.real, num_sqrt.imag))
