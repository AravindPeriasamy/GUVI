x = int(input())
count = 0
list1 = [int(i) for i in input().split()]
for i in range(len(list1)-2):
	for j in range(i+1,len(list1)-1):
		for k in range(j+1,len(list1)):
			if list1[i] + list1[j] == list1[k]:
				count += 1
print(count)
