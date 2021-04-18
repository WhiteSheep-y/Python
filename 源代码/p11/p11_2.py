# p11_2.py
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 这里我们主要演示类的继承机制，我们就不考虑检查场景边界和移动方向的问题
        # 这两部分内容在上节课的课后作业里边有，大家可以回头去看一下参考代码即可
        
        # 假设所有鱼都是一路向西游
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

# 上边几个都是食物，食物不需要有个性，所以我们直接继承Fish类的全部属性和方法即可
# 下边我们定义鲨鱼类，这个是吃货，除了继承Fish类的属性和方法，我们还要添加一个吃的方法

class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有得吃^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下！")
