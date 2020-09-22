#-*- coding: utf-8 -*-

#使用update()方法，第二个参数合并第一个参数
def Merge(dict1, dict2):
    return(dict2.update(dict1))

#初始化两个字典
dict1 = {"a": 11, "b": 22}
dict2 = {"c": 33, "d": 44}

#返回None
print(Merge(dict1, dict2))

#dict2合并了dict1
print(dict2)
