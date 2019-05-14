x, y = map(int, input().split())
list1 = list(map(int,input().split(" ")))
count = 0
for i in range(0,(x-1)):
	if abs(list1[i]-list1[i+1]) == y:
		count+=1
print(count)
