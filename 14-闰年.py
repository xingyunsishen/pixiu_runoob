#-*- coding:utf8 -*-

year = int(input("please input year:"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('{0}是闰年'.format(year))
        else:
            print('{0}不是闰年'.format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
