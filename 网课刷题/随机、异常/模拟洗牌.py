import random
n = eval(input())
random.seed(n)
l = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(l)
print(l)