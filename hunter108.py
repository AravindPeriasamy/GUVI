x = list(input())
list1 = []
out = 0
if len(x) == 1:
	out = int(x[0]) * int(x[0])
else:
	for i in x:
		list1.append(int(i))
	for i in range(len(list1)-1):
		out += (list1[i] ** list1[i+1])
	out += (list1[len(list1)-1] ** list1[0] )
print(out)
