a, b = map(int,input().split(" "))
list1 = list(map(int,input().split(" ")))
list1.insert(0,0)
one = []
two = []
for i in range(b):
	x, y = map(int,input().split(" "))
	one.append(x)
	two.append(y)
for i in range(b):
	print(sum(list1[one[i]:(two[i]+1)]))
