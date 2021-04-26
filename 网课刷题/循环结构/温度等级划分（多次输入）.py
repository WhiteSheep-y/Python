temp = input()
while temp.isalpha()!=True:
    if temp[-1]=='C':
        temp=eval(temp[0:-1])
        if temp<=0:
            print('寒冷')
        elif temp<=10:
            print('冷')
        elif temp<=20:
            print('凉爽')
        elif temp<=28:
            print('舒适')
        elif temp<=38:
            print('热')
        else:
            print('热死狗啦~~~')
        temp = input()
    else:
        print('请以C作为温度值的结尾')
        temp = input()
else:
    print('请输入一个数字')