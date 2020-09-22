#-*- coding: utf8 -*- 
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



#测试字符串和数字
print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.37'))
print(is_number('1e3'))

#测试unicode
#测试阿拉伯语
print(is_number('。'))

#测试中文数字
print(is_number('四'))
#测试版权号
print(is_number('©'))
'''
#进一步扩展
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    import unicodedata
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    if len(s) < 2:
        return False

    try:
        d = 0
        if s.startswith('-'):
            s = s[1:]
        for c in s:
            if c == '－':#全角建号
                return False

            if c == '．':#全角点号
                if d > '0':
                    return False
                else:
                    d = 1
                    continue
            unicodedata.numeric(c)
        return True
    except (TypeError, ValueError):
        pass
    return False

#测试字符串和数字
print(f'{is_number("foo")}')
print(f'{is_number("1")}')
print(f'{is_number("1.3")}')
print(f'{is_number("-1.37")}')
print(f'{is_number("1e3")}')
print(f'{is_number("2.345.6")}')
print(f'{is_number("-5.2-8")}')
print(f'{is_number("52-8")}')
print(f'{is_number("-.5")}')
print(f'{is_number("-5.")}')
print(f'{is_number(".5")}')
#测试Unicode
#测试阿拉伯语
print(f'{is_number("。")}')
print(f'{is_number("ياخشىمۇسىز")}') #维吾尔语
print(f'{is_number("六")}') #中文六

#测试全角数字
print(f'{is_number("１２３")}')
print(f'{is_number("－１２３")}')
print(f'{is_number("-１２３")}')
print(f'{is_number("１２－３")}')
print(f'{is_number("１.２３")}')
print(f'{is_number("１．２３")}')
print(f'{is_number("．２３")}')
print(f'{is_number("－．２３")}')
print(f'{is_number("１．２３")}')
print(f'{is_number("１．２．３")}')

