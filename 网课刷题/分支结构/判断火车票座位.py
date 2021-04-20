s = input()
list = ['A','B','C','D','F','a','b','c','d','f']
if 1<=int(s[0:-1])<=17 and s[-1] in list:
    if s[-1] in ['A','F','a','f']:
        print('窗口')
    elif s[-1] in ['C','D','c','d']:
        print('过道')
    elif s[-1] in ['B','b']:
        print('中间')
else:
    print("输入错误！")