n = int(input())//2+1
for i  in  range(1,n+1):
    print("{:^{width}}".format("*"*(2*i-1), width=2*n-1))

'''
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
'''