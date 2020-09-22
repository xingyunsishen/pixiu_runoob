#-*- coding: utf-8 -*-
def bubbleSort(arr):
    n = len(arr)
    #遍历所有数组元素
    for i in range(n):
        #Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+a] = arr[j+1], arr[j]

arr = [10, 0, 2, 40, 21, 11, 14]
bubbleSort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])
