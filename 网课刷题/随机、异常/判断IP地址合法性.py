try:
	s = input().split('.')
	if len(s) != 4:
	    flag = 'No'
	else:
	    for ipNum in s:
	        if eval(ipNum)>255 or eval(ipNum)<0:
	            flag = 'No'
	    else:
	        flag = 'Yes'
except:
	flag = 'No'
print(flag)