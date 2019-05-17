x = list(input())
list1 = []
out = 0
if x == 1:
	out = 1
else:
	for i in x:
		list1.append(int(i))
	for i in range(len(list1)):
		out += (list1[i] ** len(list1))
print(out)
