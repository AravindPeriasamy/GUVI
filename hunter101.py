end = int(input())
sta = 1
prime = [True for i in range(end+1)] 
p = 2
out = []
outlist = []
code = 0
while (p * p <= end): 
    if (prime[p] == True): 
        for i in range(p * p, end+1, p): 
            prime[i] = False
    p += 1
for p in range(sta, end): 
        if prime[p] and p!=1: 
            outlist.append(p)
for i in range(0,(len(outlist))):
	for j in range(0,len(outlist)):
		for z in range(0,len(outlist)):
			if (outlist[i] + outlist[j] + outlist[z]) == end:
				out.append(outlist[i])
				out.append(outlist[j])
				out.append(outlist[z])
				code = 1
				break
		if code == 1:
			break
	if code == 1:
		break
print(*out)
