from turtle import *
import turtle
pu()
fd(-250)
pd()
pensize(20)
pencolor(0/255,255/255,255/255)
seth(-40)
for i in range(1,5):
    x=255-int(i)*20
    circle(40,80)
    circle(-40,80)
    pencolor(0/255,x/255,x/255)
circle(40,40) 
fd(40)
circle(16,180)
fd(40*2/3)
done()