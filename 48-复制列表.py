#-*- coding:utf-8 -*- 
def clone_runoob(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)

print("原始列表:", li1)
print("复制后:", li2)

#使用extend()方法
def clone_runoob(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy

li1 = [1, 3, 4, 5, 6]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后:", li2)

#使用list()方法
def clone_runoob(li1):
    li_copy = list(li1)
    return li_copy

li1 = [2, 3, 4, 5, 6]
li2 = clone_runoob(li1)
print("复制前:", li1)
print("复制后:", li2)
