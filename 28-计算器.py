#-*- coding:utf-8 -*-

#定义函数
def add(x, y):
    #加法
    return x + y

def subtract(x, y):
    #减法
    return x - y

def multiply(x, y):
    #乘法
    return x * y

def divide(x, y):
    #除法
    return x / y

#用户输入
print('==' * 5, '选择运算符', '==' * 5)
print('1, 加法')
print('2, 减法')
print('3, 乘法')
print('4, 除法')
print("==" * 16)
choice = input("please input (1/2/3/4):")

num1 = int(input('please input first number:'))
num2 = int(input('please input second number:'))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':    
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':    
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':    
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print('Input Error')
