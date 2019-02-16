a = int(input())
list1 = []
for i in range(a):
	for j in input().split(" "):
		list1.append(int(j))
list1.sort()
print(*list1)
