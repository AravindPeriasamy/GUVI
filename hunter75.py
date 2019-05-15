x = int(input())
list1 = [int(e)for e in input().split()]
for i in  range(0 , (len(list1)-1)):
	if list1[i] > list1[i+1]:
		list1[i] = list1[i+1]
	else:
		list1[i] = -1
list1[(len(list1)-1)] = -1
print(*list1)
