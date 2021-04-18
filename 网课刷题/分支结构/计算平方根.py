import math
n = input()
if n.replace('.','').isnumeric():
    print("{}的平方根为{:.2f}。".format(n,math.sqrt(eval(n))))
else:
    print("请输入正确的参数。")