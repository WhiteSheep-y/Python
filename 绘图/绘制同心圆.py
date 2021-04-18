from turtle import *
r=int(input())
n=int(input())
c=input()
pencolor(c)
pensize(3)
for i in range(n):
    circle(r)
    r+=20
    pu()
    seth(-90)
    fd(20)
    seth(0)
    pd()
done()