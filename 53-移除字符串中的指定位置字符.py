#-*- coding:utf-8 -*-
test_str = "Runoob"
#输出原始字符串
print("原始字符串:" + test_str)

#移除第三个字符n
new_str = ""

for i in range(0, len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print("移除后的字符串:" + new_str)
