from random import *
m=eval(input())
n=eval(input())
seed(a=m)
l=[]
for i in range(n):
    l.append(str(randint(0,9)))
print(l)
l=set(l)
l=list(l)
l.sort()
print(l)
#print(sorted(set(l)))  #sorted()函数作用是排序后以列表形式输出