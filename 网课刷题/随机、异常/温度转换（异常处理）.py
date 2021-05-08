try:
    t = input()
    if t[-1] in ["F","f"]:
        T = (eval(t[0:-1])-32)/1.8
        print("{:.2f}C".format(T))
    elif t[-1] in ["C","c"]:
        T = (eval(t[0:-1])*1.8)+32
        print("{:.2f}F".format(T))
    else:
        print("输入错误，温度值末位只能是'C','c','F','f'")
except NameError:
    print("试图访问的变量名不存在")
except SyntaxError:
    print("存在语法错误")
except Exception as e:
    print(e)