from turtle import *
from datetime import *

def initialization():
    speed(0) #速度
    pensize(2) #笔画粗细设置为2
    # 位置调整
    pu()
    seth(-90)
    fd(400)
    seth(90)
    ht()#隐藏海龟

def base():
    pd()
    for i in range(4):
        if i%2==0:
            fd(40) #底座高40
            left(60)
        else:
            fd(120) #底座长120
            left(120)
    for i in range(4):
        if i%2==0:
            fd(40)
            right(60)
        else:
            fd(120)
            right(120)

    pu()
    fd(40)
    right(60)
    fd(120)
    left(120)
    pd()
    fd(80)

    pu()
    fd(40)
    left(60)
    fd(40)
    pd()
    fd(80)
    left(120)
    fd(120)
    seth(90)

    pu() #终点为中间最底
    #done()

def CenterPillar_D():#中柱下端
    fd(40)
    pd()
    for i in range(4):
        if i%2==0:
            fd(120) #中柱下端高120
            left(60)
        else:
            fd(40) #中柱下端宽40
            left(120)
    for i in range(4):
        if i%2==0:
            fd(120)
            right(60)
        else:
            fd(40)
            right(120)
    up()
    fd(120)
    #done()

def 外圈():#轮廓
    pd()
    right(60)
    for i in range(6):
        if i!=1 and i!=4:
            fd(320)
            left(60)
        else:
            fd(280)
            left(60)
    seth(90)
    #终点在外圈最底
    #done()

def 左圈():
    fd(40)
    left(60)
    d1,d2=280,200
    for i in range(5): #循环画规律左轮廓
        if i%2==0:
            if i!=4:
                fd(d1)
                right(60)
                d1-=40
            else:
                fd(d1-40)
        else:
            fd(d2)
            right(120)
            d2-=40
    #画不规则部份
    right(120)
    fd(160)
    right(120)
    fd(40)
    right(60)
    fd(120)
    right(60)
    pu()
    fd(80)
    seth(90)
    pd()
    for i in range(3):
        fd(160)
        right(120)
    left(120)
    fd(40)
    pu()
    left(120)
    fd(280)

def 右圈():
    left(60)
    pd()
    d1,d2=280,200
    for i in range(6): #循环画规律右轮廓
        if i%2==0:
            fd(d1)
            left(60)
            d1-=40
        else:
            fd(d2)
            left(120)
            d2-=40
    #画不规则部份
    seth(90)
    fd(40)
    seth(-90)
    fd(120)
    right(120)
    fd(120)
    left(60)
    fd(40)
    left(120)
    fd(160)
    right(120)
    fd(40)
    right(60)
    fd(160)
    #done()
    #终点为右圈左上角端点

def 上圈():
    seth(90)
    fd(40)
    left(60)
    d1,d2=280,240
    for i in range(4):
        if i%2==0:
            fd(d1)
            right(120)
            d1-=40
        else:
            fd(d2)
            right(60)
            d2-=40
    left(60)
    fd(40)
    left(120)
    fd(40)
    left(60)
    fd(280)
    #done()
    #终点在右圈最右上角端点

def CenterPillar_U():#中柱上端
    #中间三条线
    left(120)
    fd(280)
    left(120)
    pu()
    fd(80)
    pd()
    fd(160)
    pu()
    fd(40)
    pd()
    fd(200)
    right(60)
    fd(40)
    right(120)
    fd(200)
    pu()
    fd(40)
    pd()
    fd(240)
    left(120)
    fd(40)
    left(60)
    pu()
    fd(40)
    pd()
    fd(160)
    pu()
    fd(80)
    pd()
    fd(160)
    left(60)
    fd(40)

def other():
    left(120)
    fd(200)
    left(60)
    fd(320)
    #上面两条线
    left(180)
    fd(80)
    left(60)
    pu()
    fd(40)
    pd()
    fd(200)
    right(60)
    fd(200)
    #终点为

def C_time():
    pu()
    seth(-90)
    fd(470)
    seth(180)
    fd(40)
    day=datetime(2021,6,10)
    write("软2  杨倚天  {}".format(day.strftime("%Y-%m")),move=True,font=("宋体",23,"bold"))
    fd(30)
    done()

def main():
    initialization()
    base()
    CenterPillar_D()
    外圈()
    左圈()
    右圈()
    上圈()
    CenterPillar_U()
    other()
    C_time()

main()