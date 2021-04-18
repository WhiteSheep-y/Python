# p12_1.py
class Rectangle:
    """
    我们定义一个矩形类，
    需要长和宽两个参数，
    拥有计算周长和面积两个方法。
    我们需要对象在初始化的时候拥有“长”和“宽”两个参数，
    因此我们需要重写__init__()方法，因为我们说过，
    __init__()方法是类在实例化成对象的时候首先会调用的一个方法，
    大家可以理解吗？
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getPeri(self):
        return (self.x + self.y) * 2
    
    def getArea(self):
        return self.x * self.y
