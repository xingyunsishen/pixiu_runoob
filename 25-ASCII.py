#-*- coding:utf-8 -*-

#接收用户输入的字符
c = input('please input a character:')
#用户输入ASCII码值
a = int(input('请输入一个数字:'))

print(c + '的ASCII码为:', ord(c))
print(a , "的对应的字符为:", chr(a))
