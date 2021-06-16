import random
random.seed(10)
start, end = map(int, input().split())
l = []
m = {}
for i in range(100):
    l.append(random.randint(start, end))
for i in l:
    m[i] = m.get(i, 0)+1
for i in sorted(m.keys()):
    print("{} {}".format(i,m.get(i)))