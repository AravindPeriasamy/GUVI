end = int(input())
sta = 1
prime = [True for i in range(end+1)] 
p = 2
sum = 0
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
for i in outlist:
	if str(i).endswith('3'):
		sum += i
print(sum)
