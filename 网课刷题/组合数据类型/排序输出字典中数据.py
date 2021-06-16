dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20}
dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}
n=eval(input())
print(sorted(dic1)[:n])
print(sorted(dic2.items(),key=lambda d: d[1])[:n])