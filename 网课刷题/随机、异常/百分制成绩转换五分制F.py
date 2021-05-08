try:
  n = eval(input())
  if 0<=n<60:
    print("E")
  elif n<70:
    print("D")
  elif n<80:
    print("C")
  elif n<90:
    print("B")
  elif n<=100:
    print("A")
  else:
    print("data error!")
except :
  print("data error!")