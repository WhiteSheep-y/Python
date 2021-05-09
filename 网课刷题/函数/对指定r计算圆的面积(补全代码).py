import math
def getCircleArea(r):
    return math.pi*r**2
n=int(input())
for i in range(n):
    r=float(input())
    print('{:.3f}'.format(getCircleArea(r)))#调用getCircleArea并打印结果
print('END.')