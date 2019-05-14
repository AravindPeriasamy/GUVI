x, y = map(int, input().split())
list1 = list(map(int,input().split(" ")))
count = 0
for i in range(0,(x-1)):
	for j in range(i+1,x):
		if abs(list1[i]-list1[j]) == y:
			count+=1
print(count)
