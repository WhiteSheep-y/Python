import random
k = 0
n = input('请输入您猜测的数字：')
ans = random.randint(0,30)
while True:
    if n.isdigit():
        n = int(n)
        k+=1
        if n<ans:
            print('遗憾，太小了！')
        elif n>ans:
            print('遗憾，太大了！')
        else:
            break
    else:
        print('请输入一个数字！')
    n = input('请输入您猜测的数字：')
print("预测{}次，你猜中了！".format(k))