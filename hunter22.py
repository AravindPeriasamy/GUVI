list1 = list(map(int,input().split(" ")))
product = 1
list2 = []
for i in list1:
	product = product * i
for i in list1:
	list2.append((product//i))
print(*list2)
