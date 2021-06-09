num = eval(input())
n = int(input())
List = []
for i in range(len(num)):
    List.insert(i,max(num))
    num.remove(max(num))
print(List[n-1])