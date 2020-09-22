#-*- coding:utf-8 -*-

def search(arr, n, x):
    for i in range(0, n):
        if(arr[i] == x):
            return i;
    return -1;

# 在数组中arr中查找字符D
arr = ['A', 'B', 'C', 'D', 'E']
x = 'D'
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("元素不在数组中")
else:
    print("元素在数组中的索引:", result)
