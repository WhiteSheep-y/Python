# p4_11.py
bingo = '清蒸'
answer = input('小甲鱼是清蒸还吃还是炖了好吃？')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）：')

print('对嘛，只有清蒸才能原汁原味~')
