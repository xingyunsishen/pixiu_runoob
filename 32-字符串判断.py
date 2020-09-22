#-*- coding:utf-8 -*-

#测试
print("测试1")
str = 'runoob.com'

print(str.isalnum())  #判断所有字符都是数字或者字母
print(str.isalpha())  #判断所有的字符都是字母
print(str.isdigit())  #所有字符都是数字
print(str.islower())  #所有字符都是小写
print(str.isupper())  #所有字符都是大写
print(str.istitle())  #所有单词首字母大写
print(str.isspace())  #所有字符都是空白字符、\t、\n、\r
print('==' * 10)

#测试2
print('测试2')
str = 'runoob'
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())
