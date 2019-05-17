x = int(input())
list1 = []
for i in range(x,0,-1):
	for j in range(i):
		list1.append('1')
	print(*list1)
	list1 = []
