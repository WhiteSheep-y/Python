def fun(n):
    if n==1 or n==2 :
        return 1
    return fun(n-1)+fun(n-2)
n=eval(input())
sum=fun(n)
sum2=fun(n-1)
print("{} {:.3f}".format(sum,sum2/sum))