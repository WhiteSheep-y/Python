x = input()
if x.lstrip("-").isdigit():
    if x.find("-")!=-1:
        print("-{}".format(x.lstrip("-")[::-1]))
    else:
        print(x[::-1])
else:
    print("输入有误！")
