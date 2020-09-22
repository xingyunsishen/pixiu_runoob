#-*- coding: utf-8 -*-
'''
30个人在一条船上，超载，需要下去一半人
30人占成一排，排队的位置即为他们的编号
报数，从1开始，数到9的人下船
如此循环，知道船上还剩余15人为止，问下去的都有几号
'''
people = {}

for x in range(1, 31):
    people[x] = 1

check = 0
i = 1
j = 0
while i <= 31:
    if i == 31:
        i = 1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check += 1
            if check == 9:
                people[i] == 0
                check = 0
                print('{}号下船了'.format(i))
                j += 1
            else:
                i += 1
                continue
