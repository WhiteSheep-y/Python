ls=eval(input())
l1=[]
l2=[]
for i in range(len(ls)):
    if ls[i]==0:
        l1.append(0)
    else:
        l2.append(ls[i])
print(l2+l1)