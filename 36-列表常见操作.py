#-*- coding: utf-8 -*-
'''
#定义列表
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L)

#索引、切片
print('L[0] =', L[0])
print('L[0:3] =', L[0:3])
print('L[0::2] =', L[0::2])
print('L[:2:] =', L[:2:])
print('L[::2] =', L[::2])
print('L[::-1] =', L[::-1])
print('L[-1] =', L[-1])
print('L[-4] =', L[-4])
print('L[-1:-4] =', L[-1:-4])
print('L[-4:-1] =', L[-4:-1])
print('L[-4:] =', L[-4:])
print('L[1:-1] =', L[1:-1])

#增加元素
n = input('please input n:')
L.append(n)
print(L)
m = int(input('请输入要插入的位置:'))
p = input('请输入要插入的内容:')
L.insert(m, p)
print(L)
s = input('please input s:')
L.extend([s])
print(L)

#搜索
w = input('请输入要搜索的内容：')
print(w, '在列表位置:', L.index(w))

#list运算
l_01 = ['apple', 'banana']
l_01 = l_01 + ['Orange']
print(l_01)
l_01 += ["potato"]
print(l_01)
l_01 = l_01 * 3
print(l_01)

#使用join连接list
s_01 = {'ID': 10001, 'Dep': "SRE", 'Name': '张三'}
print(["%s=%s" %(k, v) for k, v in s_01.items()])
print(";".join(["%s=%s" %(k, v) for k, v in s_01.items()]))

#分割字符串
l_01 = ["apple", "orange", "banana", "potato", "watermelon"]
res = ":".join(l_01)
print(res)
res.split(":")
print(res)
res.split(":", 1)
print(res)
#映射解析
l_01 = [1, 2, 3, 4]
print(l_01)
res = [elem * 2 for elem in l_01]
print(res)
#dictionary中的解析
s = {"UID": 10001, "Name": "zhangsan", "Age": 24, "Dep": "Sre"}
print('s.keys() =', s.keys())
print('s.values() =', s.values())
res = s.items()
print(res)
print([k for k, v in s.items()])
print([v for k, v in s.items()])
print(["%s=%s" %(k, v) for k, v in s.items()])
'''
#list过滤
l_01 = ['a', 'b', 'c', 'd', 'e', 'apple', 'banana']
print([elem for elem in l_01 if len(elem) > 1])
print([elem for elem in l_01 if elem != "b"])
print([elem for elem in l_01 if l_01.count(elem) == 1])
