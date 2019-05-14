x, y = map(int,input().split())
list1 = list(map (int,input().split(" ")))
for i in  range(y):
	temp=list1.pop(0)
	list1.append(temp)
print(*list1)
