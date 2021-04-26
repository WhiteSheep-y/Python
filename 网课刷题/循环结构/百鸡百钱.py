for i in range(0,20):
    for j in range(0,33):
        for k in range(0,300,3):
            if i+j+k==100 and i*5+j*3+(k/3)==100:
                print(i,j,k,sep=' ')