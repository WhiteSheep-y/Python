import math
mileage,time = eval(input())
if mileage<=3 :
    price = 13
elif mileage<=15 :
    price = 13+(mileage-3)*2.3
else:
    price = 13+12*2.3+(mileage-15)*2.3*1.5
print(int(price+time))