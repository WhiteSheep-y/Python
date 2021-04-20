import math
x,y = input().split(',')
x=int(x)
y=int(y)

if (x**3-x*y)<0 :
    print("公式计算参数有误！")
elif y==0 :
    print("公式计算参数有误！")
else:
    if x==0 :
        print("0.00")
    else:
        z = (x-math.sqrt(x**3-x*y))/(2*math.e*y)
        print("{:.2f}".format(z))