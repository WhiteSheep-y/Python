m = input()
if m[0:3] == "RMB":
    print("USD{:.2f}".format(eval(m[3:])/6.78))
else:
    print("RMB{:.2f}".format(eval(m[3:])*6.78))