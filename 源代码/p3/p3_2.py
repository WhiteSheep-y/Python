# p3_2.py
import random

secret = random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
times = 1

while (guess != secret) and (times < 3):
    if guess > secret:
        print("哥，大了大了~~~")
    else:
        print("嘿，小了小了~~~")

    temp = input("请再试试吧：")
    guess = int(temp)
    times = times + 1

if times < 3:
    print("哎呀，你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励噢~")
else:
    print("唔，给三次机会都猜错，不跟你玩了！")
