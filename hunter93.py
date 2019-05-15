list1 = [e for e in input().split(" ")]
count = 0
outlist = []
for i in list1:
	i.split()
	string = ""
	for j in range(0,len(i)):
		if j%2 == 0:
			string += i[j].upper()
		else:
			string += i[j]
	outlist.append(string)
print(*outlist)
