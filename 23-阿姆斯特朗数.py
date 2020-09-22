#-*- coding:utf-8 -*- 

num = int(input('please input a number:'))

#初始化变量sum
sum = 0

#指数
n = len(str(num))

#检测
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

#输出结果
if num == sum:
    print(num,"是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")

#获取指定区间内的阿姆斯特朗数
#接收区间值
lower = int(input('please input a start number:'))
upper = int(input('please input a end number:'))

for num in range(lower, upper + 1):
    #初始化sum
    sum = 0

    #指数
    n = len(str(num))

    #检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if num == sum:
        print(num)

print()
