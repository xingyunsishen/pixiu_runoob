#-*- coding:utf8 -*-
while True:
    a = float(input("please input a:"))
    b = float(input("please input b:"))
    c = float(input("please input c:"))
    
    #判断输入数能否构成三角形
    #构成三角形的条件是任意两条边之和大于第三边
    if a + b > c and a + c > b and b + c > a:
        print("是三角形")
    else:
        print("输入有误，请重新输入") 
        continue
    
    #半周长
    r = (a + b +c) / 2
    
    #计算面积
    s = (r * (r - a) * (r - b) * (r - c)) ** 0.5
    print("三角形的面积为:%0.2f" %s)
    break

