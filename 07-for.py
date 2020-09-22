#-*- coding:utf8 -*- 

for x in range(1, 11):

    print(x, 'hello world')
#for循环遍历字符串
for letter in 'Python':
    print'Current Letter:', letter
#for循环遍历列表
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print'Current fruit:', fruit
print"Good Bye~"

for index in range(len(fruits)):
    print'Current Fruit:', fruits[index]

print"Good Bye!"
#for循环遍历元组
t = (2, 3, 4, 'a', 'b')
for x in t:
    if  x > 3:
        print x

#for循环遍历字典
d = {'ID': '1001', 'Name': 'sihen', 'ID': '1002', 'Name': 'zhangsan', 'ID': '1003', 'Name': 'lisi'}
for a in d: #此时x遍历只能将key取出来,且结果跟预想的不一样
    print a
    print d[a]
print d.items()

for k, v in d.items():
    print k,v
d = {1:11, 2:22, 3:33, 4:44}
for x in d:
    print d[x]
print d.items()

for k, v in d.items():
    print k, v

for i in range(1, 101, 2):
    print i
    sum += i
    print sum
