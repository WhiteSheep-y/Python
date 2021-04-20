import math
mileage,time = input().split(',')
mileage=eval(mileage)
time=eval(time)
if mileage<=3 :
    price = 13
elif mileage<=15 :
    price = math.fsum([13,(mileage-3)*2.3])
else:
    price = math.fsum([13,(mileage-3)*2.3,(mileage-15)*2.3*1.5])
print("{:d}".format(math.floor(price+time)))