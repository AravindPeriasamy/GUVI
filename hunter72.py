x = [str(i) for i in input().split()]
for i in range(0,len(x),2):
	x[i]=x[i].replace(".","")
	x[i] = x[i][::-1]
print(*x)
