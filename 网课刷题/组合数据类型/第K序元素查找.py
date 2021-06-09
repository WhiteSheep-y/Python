import queue
s=eval(input())
k = eval(input())
pq = queue.PriorityQueue()
for v in s:
    pq.put(v)
    #维护一个大小为k的优先队列，使其中保存列表中最大k个数
    if pq.qsize()>k:
        pq.get()
print(pq.get())#弹出队列中最小的数

'''
num = eval(input())
n = int(input())
List = []
for i in range(len(num)):
    List.insert(i,max(num))
    num.remove(max(num))
print(List[n-1])
'''