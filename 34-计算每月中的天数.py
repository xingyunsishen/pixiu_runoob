#-*- coding:utf-8 -*-
import calendar

#接收用户输入
month = int(input('please input month:'))
year = int(input('please input year:'))
monthRange = calendar.monthrange(year, month)
#输出结果是一个元组，元组中的第一个元素是这个月的第一天是周几(0-6)，
#第二个元素表示这个月有多少天
print(monthRange)
print('%d月的第一天是周%d' %(month, monthRange[0]))
print(calendar.mdays[month])  #只输出每个月的天数
