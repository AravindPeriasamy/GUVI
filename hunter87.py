x ,y = map(int,input().split(" "))
list1 = [int(i) for i in input().split()]
count = 0
for i in list1:
	if i <= y:
		count += 1
print(count)
