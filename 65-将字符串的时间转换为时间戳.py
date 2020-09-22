#-*- coding:utf-8 -*-
import time

a1 = "2020-09-07 14:55:12"

#先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

#转换为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

#格式转换
a2 = "2020/09/07 15:12:55"
#先转换为时间数组，然后转换为其他格式
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)
