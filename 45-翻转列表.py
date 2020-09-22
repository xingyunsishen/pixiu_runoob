#-*- coding: utf-8 -*-
def Reverse(lst):
    return [ele for ele in reversed(lst)]

lst = [10, 12, 14, 16, 19, 18]
print(Reverse(lst))

def Reverse(lst):
    lst.reverse()
    return lst

lst = [10, 13, 154, 150, 20]
print(Reverse(lst))

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 13, 154, 150, 20]
print(Reverse(lst))
