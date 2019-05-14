x, y = map(int,input().split(" "))
list1 =[int(n) for n in input().split()]
while y in list1:
	list1.remove(y)
if not list1:
	print("empty")
else:
	print(*list1)
