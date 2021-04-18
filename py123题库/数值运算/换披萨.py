big=eval(input())
small=eval(input())
b_area=int((big*2.54/2)**2*3.14)
s_area=t=int((small*2.54/2)**2*3.14)
n=1
while t<b_area:
    t+=s_area
    n+=1
print(n)