x = int(input())
list2 = list(map(int,input().split(" ")))
list4= list(map(int,input().split(" ")))
list3 = []
for i in range(x):
	list3.append(list2[i]+list4[i])
print(*list3)
