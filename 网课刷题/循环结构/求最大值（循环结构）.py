n = eval(input())
max = -1
if n<=0:
    print("ERROR")
else:
    for i in range(n):
        x = eval(input())
        if x>max :
            max = x
    print("max={}".format(max))