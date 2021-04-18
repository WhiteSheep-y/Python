t = input()
if t[-1] in ["F","f"]:
    T = (eval(t[0:-1])-32)/1.8
    print("{:.2f}C".format(T))
elif t[-1] in ["C","c"]:
    T = (eval(t[0:-1])*1.8)+32
    print("{:.2f}F".format(T))
else:
    print("输入格式错误")
