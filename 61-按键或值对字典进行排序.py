#-*- coding:utf-8 -*-
def dictionary():
    #声明一个空字典
    key_value = {}

    #初始化
    key_value[1] = 2
    key_value[2] = 1
    key_value[3] = 13
    key_value[4] = 20
    key_value[5] = 21
    key_value[6] = -10

    print("=="*5, "排序前，原字典:", "=="*5)
    print(key_value)
    print('=='*5, "按key排序", '=='*5)

    for i in sorted(key_value):
        print((i, key_value[i]))
    print("=="*5, "按value排序", "=="*5)
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))

def main():
    #调用函数
    dictionary()

#主函数
if __name__ == "__main__":
    main()

#字典列表排序
list = [{"name":"pdd", "age":4}, 
        {"name":"runoob", "age":7},
        {"name":"google", "age":200}, 
        {"name":"wiki", "age":100}]

#通过age升序排列
print("=="*5, "通过age升序排列", "=="*5)
print(sorted(list, key = lambda i: i['age']))
print()
#先按age排序，再按name排序
print("=="*5, "先age，再name", "=="*5)
print(sorted(list, key = lambda i:(i['age'], i['name'])))
print()

#按age降序排列
print("=="*5, "列表通过age降序", "=="*5)
print(sorted(list, key = lambda i: i['age'], reverse=True))

