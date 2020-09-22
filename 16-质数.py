#-*- coding:utf-8 -*-

#接收用户输入
num = int(input('please a number:'))

#质数大于1
if num > 1:
    #查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘以", num // i, "是", num)
            break
    else:
        print(num, "是质数")
#如果输入的数小于或等于1，不是质数
else:
    print(num, "不是质数")
