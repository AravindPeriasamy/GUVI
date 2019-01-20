start, end = map(int, input().split(" "))
list1 = []
for i in range(start+1 , end):
	if i%2 == 1:
		list1.append(i)
print(*list1)
