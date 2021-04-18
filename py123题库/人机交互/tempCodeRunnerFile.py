def loop(n):
    # 你的代码写在这里
    sum=0
    for i in range(n):
        sum+=i
    print(sum)

if __name__ == '__main__':
    n = int(input())      # 输入一个整数
    loop(n)               # 调用函数运算
