#-*- coding:utf-8 -*-

#定义函数
def _sum(arr, n):
    #使用内置的sum函数计算
    return(sum(arr))

#调用函数
arr = []
#数组元素
arr = [12, 13, 14, 15]

#计算数组元素的长度
n = len(arr)

ans = _sum(arr, n)

#输出结果
print('数组元素之和为', ans)
