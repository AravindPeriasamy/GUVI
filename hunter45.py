x=int(input())
list1 = list(map(int,input().split(" ")))
count = 0
for i in range(1,(x+1)):
	if (i+x) in  list1:
		count+=1
print(count)
