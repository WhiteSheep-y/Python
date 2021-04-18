from turtle import *
from typing import ByteString
pu()
fd(-450)
pd()
pensize(3)
pencolor("blue")
fillcolor("yellow")
begin_fill()
for i in range(3,11):
    circle(50,360,int(i))
    pu()
    fd(120)
    pd()
circle(50)
end_fill()
done()