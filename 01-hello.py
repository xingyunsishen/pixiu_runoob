#!~/.virtualenv/runoob/bin/python
print("Python 3")
if True:
    print("True")
else:
    print("False")

sumnum = 1 + 2 + 3 + 4 + \
         5 + \
         6 + \
         7 + \
         8 + \
         9 + \
         0
print(sumnum)

str = 'Runoob'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[:2])
print(str[::2])
print(str[::-1])
print(str * 2)
print(str + 'Python3' + '教程')

x = 'a'
y = 'b'
print(x)
print(y)
print('--' * 20)
print(x, end='')
print(y, end='')
print()

import sys
print('==' * 10, end = '')
print('Python import mode', end='')
print('==' * 10)
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为:', sys.path)

from sys import argv, path
print('++' * 10, end = '')
print('Python import mode', end = '')
print('++' * 10)
print('path:', path)

