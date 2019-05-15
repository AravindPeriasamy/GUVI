end = int(input())
sta = 1
prime = [True for i in range(end+1)] 
p = 2
outlist = []
while (p * p <= end): 
    if (prime[p] == True): 
        for i in range(p * p, end+1, p): 
            prime[i] = False
    p += 1
for p in range(sta, end): 
        if prime[p] and p!=1: 
            outlist.append(p)
if not outlist:
	outlist.append(0)
print(*outlist)
