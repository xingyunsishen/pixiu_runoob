#-*- coding:utf-8 -*-
d_01 = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

#输出原始字典
print("移除前:" + str(d_01))

#使用del移除Zhihu
del d_01['Zhihu']
print('移除后:' + str(d_01))

#移除不存在的key会报错
#del d_01["Cunzai"]
#print("移除后:" + str(d_01))
#使用pop()移除
d_01 = {"Dafa": 1, "Xiyue":  2, "Jichu": 3, "Ditie": 4}

#输出原始字典
print("移除前:" + str(d_01))

#移除后
d_02 = d_01.pop("Jichu")
print("移除后:" + str(d_01))
print("移除的key对应的value为:" + str(d_02))

#使用pop()移除没有的key不会发生异常
d_03 = d_01.pop('Yida', '该键(key)不存在')
print("字典移除后:" + str(d_01))
print("移除的值:" + str(d_03))

#使用items()移除
d_01 = {"Runoob": 1, "Google": 2, "Zhihu": 3, "Yahoo": 4}

#输出原始字典
print("字典移除前:" + str(d_01))

#使用pop移除Zhihu
d_04 = {key:val for key, val in d_01.items() if key != 'Zhihu'}
print("字典移除后:" + str(d_04))
