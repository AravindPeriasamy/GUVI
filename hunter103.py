x = int(input())
for i in range(1,x+x,2):
	list1 = []
	for j in range(0,i):
		list1.append('1')
	print(*list1)
