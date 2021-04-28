n = eval(input())
result =0
add = 1
k = 0
while add>n:
    add = 1/(2*k+1)
    result+=(-1)**k*add
    k+=1
result+=(-1)**k*add
print("{:.6f}".format(result*4))