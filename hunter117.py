x = list(input())
list1 = []
out = 0
for i in x:
	list1.append(int(i))
for i in range(len(list1)):
		out += (list1[i] ** i)
print(out)
