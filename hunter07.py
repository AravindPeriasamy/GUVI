num=int(input())
list1 = list(map(int, input().split(" ")))
list2 = []
for i in range(0,len(list1)):
	if i%2 == 0:
		if list1[i]%2 != 0:
			list2.append(list1[i])
	else:
		if list1[i]%2 == 0:
			list2.append(list1[i])
print(*list2)
