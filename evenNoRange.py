starts, ends = map(int, input().split(" "))
list1 = []
for i in range(starts+1 , ends):
	if i%2 == 0:
		list1.append(i)
print(*list1)
