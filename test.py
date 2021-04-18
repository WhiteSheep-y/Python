import math
inStr = input()
if inStr.replace('.','').isdigit():
    print('{}的平方根为{:.2f}。'.format(inStr,math.sqrt(eval(inStr))))
else:
    print('请输入正确的参数。')