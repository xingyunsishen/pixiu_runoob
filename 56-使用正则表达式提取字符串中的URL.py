#-*- coding:utf-8 -*-
import re

def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url

string = "Runoob的网页地址为:https://www.runoob.com, Google的网页地址：https://www.google.com"
print("Urls:", Find(string))

