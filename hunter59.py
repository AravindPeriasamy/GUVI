x = int(input())
list1 = list(map(int,input().split(" ")))
list2 = list(map(int,input().split(" ")))
list3 = []
for i in range(x):
	list3.append(list1[i]+list2[i])
print(*list3)
