#-*- coding:utf-8 -*-
import sys
A = [10, 20, 2, 31, 0, 1, 23]
for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("排序后的数组:")
for i in range(len(A)):
    print("%d"%A[i])
