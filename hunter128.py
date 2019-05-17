x = input()
outlist = []
for i in range(len(x)-1):
	for j in range(i+1,len(x)):
		string = x[i:j+1]
		if string == string[::-1]:
			outlist.append(string)
outlist.sort(key=len)
for i in outlist:
	print(i)
