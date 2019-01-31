num=int(input())
list2 = []
list1 = list(map(int, input().split(" ")))
for i in range(0,len(list1)):
	if i==list1[i]:
		list2.append(i)
if len(list2) > 0:
	print(*list2)
else:
	print(-1)
