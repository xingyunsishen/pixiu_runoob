#-*- coding: utf-8 -*-

import datetime

def getYesterday():
    today = datetime.date.today()
    print('今天是:', today)
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    return yesterday

print(getYesterday())

def GetYesterDay():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

print('昨天是', GetYesterDay())
