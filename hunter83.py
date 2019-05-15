x = list(input())
outlist = []
for i in range(0,(len(x)-1)):
	temp = x.copy()
	if x[i] == x[i+1]:
		temp.pop(i)
		outlist.append(int("".join(temp)))
maximum = max(outlist)
print(maximum)
