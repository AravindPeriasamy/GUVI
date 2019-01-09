start, end = map(int,input().split(" "))
prime = [True for i in range(end+1)] 
p = 2
count = 0
while (p * p <= end): 
    if (prime[p] == True): 
        for i in range(p * p, end+1, p): 
            prime[i] = False
    p += 1
for p in range(start, end+1): 
        if prime[p]: 
            count+=1
print(count)
