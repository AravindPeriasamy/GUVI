starts, ends = map(int, input().split(" "))
for i in range(starts+1 , ends):
	if i%2 == 0:
		print(i,end="\t")
