x = input()
while x.isalpha()!=True:
    y = input()
    if y.isalpha()!=True:
        x = eval(x)
        y = eval(y)
        if x==0 or y==0 :
            print("x={}\ny={}".format(x,y))
        else:
            if x>0 :
                if y>0 :
                    print("Q1")
                else: 
                    print("Q4")
            else:
                if y>0 :
                    print("Q2")
                else:
                    print("Q3")
    else:
        print('EXIT')
        break
    x = input()
else:
    print('EXIT')