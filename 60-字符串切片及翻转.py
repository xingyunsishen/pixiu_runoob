#-*- coding:utf-8 -*-
#从给定的字符串头部和尾部截取指定数量的字符串，然后将其翻转拼接
def rotate(input, d):
    Lfirst = input[0 : d]
    Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]

    print("头部切片翻转:", (Lsecond + Lfirst))
    print("尾部切片翻转:", (Rsecond + Rfirst))

if __name__ == "__main__":
    input = "Runoob"
    d = 2 #切片长度，截取两个字符
    rotate(input, d)
