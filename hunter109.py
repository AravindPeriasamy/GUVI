x = int(input())
list1 = [str(i).lower() for i in input().split()]
list1.sort()
for i in list1:
	print(i)
