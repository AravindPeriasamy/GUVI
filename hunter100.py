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
for i in range(0,(len(outlist)+1)):
	for j in range(i+1,len(outlist)):
		if outlist[i]+outlist[j] == end:
			out.append(outlist[i])
			out.append(outlist[j])
			code = 1
			break
	if code == 1:
		break
print(*out)
