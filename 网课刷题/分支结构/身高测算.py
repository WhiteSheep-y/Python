import math
fa = eval(input())
ma = eval(input())
sex = input()
if sex=="男":
    ans = math.floor((fa+ma)*1.08/2)
    print(ans)
elif sex=="女":
    ans = math.floor((fa*0.923+ma)/2)
    print(ans)
else:
    print("无对应公式")