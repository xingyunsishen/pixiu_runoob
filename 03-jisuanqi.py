#-*- coding:utf8 -*-
import sys
running = True
while running:
    try:
        t = int(input('please input a number: '))
        p = int(input('please input a number: '))
    except EOFError:
        break
    print('operator + result\n', t + p)
    print('operator - result\n', t - p)
    print('operator * result\n', t * p)
    print('operator / result\n', t / p)
