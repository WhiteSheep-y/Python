def getnum():
    nums=[]
    x=input()
    while x!="":
        nums.append(eval(x))
        x=input()
    return nums
    
inputNums = getnum()
print(inputNums)