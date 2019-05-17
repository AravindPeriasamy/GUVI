x = list(input())
list1 = []
for i in x:
	if x.count((i)) == 1 and i not in list1:
		list1.append(i)
output = "".join(list1)
print(output)
