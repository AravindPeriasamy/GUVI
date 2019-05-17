x = int(input())
count = 0
list1 = [int(i) for i in input().split()]
for i in range(len(list1)-1):
	for j in range(i+1,len(list1)):
		if list1[i]<list1[j]:
			count += 1
print(count)
