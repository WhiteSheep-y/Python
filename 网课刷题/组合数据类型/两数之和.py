nums=[]
nums=list(map(int,input().split()))
t=int(input())
x=0
for i in nums:
    for j in range(nums.index(i)+1,len(nums)):
        if nums[j]==t-i:
            x=1
            print(nums.index(i),j)
            break
    if x==1:
        break
if x==0:
    print("Fail")