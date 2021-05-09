def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input()) #读入并转换为整数类型
if isPrime(num):  #调用isPrime函数判断num是否为素数
    print('yes')
else:
    print('no')