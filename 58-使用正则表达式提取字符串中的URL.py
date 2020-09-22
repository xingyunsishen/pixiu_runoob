#-*- coding:utf-8 -*-
import re

def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url

string = 'Runoob的网页地址：https://www.runoob.com，Google的网页地址为:https://www.google.com' 
print("Urls:", Find(string))

#注意：(?:x) 匹配x但是不记住匹配项，这种括号叫作非捕获括号，使得能够定义与正则表达式运算符一起使用的自表达式。如：/(?:foo){1,2}。如果表达式是/foo{1, 2}/,{1, 2}将只应用于'foo'的最后一个字符'o'；如果使用非捕获括号，则{1, 2}会应用于整个'foo'单词。
