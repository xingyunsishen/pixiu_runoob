#-*- coding:utf-8 -*-

#使用列表进行反转
str = "Runoob"
print(str[::-1])

#使用reversed()

str = "www.runoob.com"
print(''.join(reversed(str)))

#lambda+reduce

from functools import reduce

str = 'Runoob'
print(reduce(lambda x, y: y + x, str))
