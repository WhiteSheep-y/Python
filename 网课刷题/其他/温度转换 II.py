t = input()
if t[0] in ["F","f"]:
    T = (eval(t[1:])-32)/1.8
    print("C{:.2f}".format(T))
elif t[0] in ["C","c"]:
    T = (eval(t[1:])*1.8)+32
    print("F{:.2f}".format(T))
else:
    print("输入格式错误") 