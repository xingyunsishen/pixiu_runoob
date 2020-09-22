#-*- coding:utf-8 -*- 
"""
A、B、C、D、E五人组团夜里去捕鱼，天亮后，A第一个醒来，A将鱼分为5份，把多余的
一条鱼丢掉了，拿走自己那一份，B第二个赶来，也将鱼分为5份，把多余的一条鱼也
丢掉了，并拿走属于自己的那份，C、D、E依次按同样的方法拿走属于自己的鱼
问他们一共捕了多少条鱼？
"""
def main():
    fish = 1
    while True: 
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f"一共捕了{fish}条鱼")
            break
        fish += 1

if __name__ == '__main__':
    main()
