n = input()
if n.isdigit() and int(n)>1:
    flag=0
    for i in range(int(n),0,-1):
        for j in range(2,i-1):
            flag=0
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i)
            break
else:
    print("请输入一个大于1的正整数！")