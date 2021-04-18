from turtle import *
import turtle
turtle.setup(650,350,200,200) #窗体大小
pu()  #pen up 抬起画笔
fd(-250) #forward向前
pd() #pen down 放下画t笔
pensize(5) #画笔尺寸
pencolor("blue") #画笔颜色
seth(-40) #set heading 方向
for i in range(3): #循环
    circle(40,80)
    circle(-40,80)
circle(40,40) 
fd(40)
circle(16,180) #折回
fd(40*2/3)
done()