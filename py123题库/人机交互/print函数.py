def s_num(n):
    # 在此处写你的代码
    for i in range(1,n+1):
        print(i,end="")

if __name__ == '__main__':
    n = int(input())       # 输入一个正整数
    s_num(n)               # 调用函数
