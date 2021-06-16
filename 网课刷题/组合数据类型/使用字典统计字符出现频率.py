try:
    s = map(int, input().split(','))
    m = {}
    for i in s:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    print(m)
except:
    print("请输入一个数字。")