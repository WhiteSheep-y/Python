def fun(n):
    j=2
    for i in range(n):           
        while(True): 
            if str(j)[::-1] == str(j):
                for k in range(2, j // 2 + 1):
                    if j % k == 0:
                        j += 1
                        break
                else:
                    print(j, end=" ")
                    j += 1
                    break
            else:
                j += 1
            # for k in range(2,j // 2 + 1):
            #     if j%k==0:
            #         j+=1
            #         break
            # else:
            #     if str(j)[::-1]==str(j):
            #         print(j,end=" ")
            #         j+=1
            #         break
            #     else:
            #         j+=1
n=eval(input())
fun(n)