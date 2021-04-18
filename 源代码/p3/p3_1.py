# p3_1.py
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)

while guess != 8:
    if guess > 8:
        print("哥，大了大了~~~")
    else:
        print("嘿，小了小了~~~")
        
    temp = input("请再试试吧：")
    guess = int(temp)

print("哎呀，你是小甲鱼心里的蛔虫吗？！")
print("哼，猜中了也没有奖励噢~")