#-*- coding:utf-8 -*-

#write file
with open("write.txt", 'wt') as out_file:
    out_file.write("该文本会写入到文件中\n看到了吧！")

#read file
with open("write.txt", 'rt') as in_file:
    text = in_file.read()

print(text)
