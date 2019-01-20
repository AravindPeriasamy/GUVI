n,a,d = map(int,input().split(" "))
list = []
for i in range(1,n+1):
	ap = a+(i-1)*d
	list.append(ap)
print(sum(list))
