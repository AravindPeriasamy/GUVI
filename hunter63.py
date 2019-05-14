x = int(input())
list1 =[int(n) for n in input().split()]
list2 = []
for i in range(0,x-1):
	list2.append(max(list1[i+1:(len(list1))]))
list2.append(0)
print(*list2)
