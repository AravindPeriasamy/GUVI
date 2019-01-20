start, end = map(int, input().split(" "))
for i in range(start+1 , end):
	if i%2 == 1:
		print(i,end="\t")
