string = input()
string.split()
even = []
odd = []
outlist=""
for i in range(0,len(string)):
	if (i+1)%2==0:
		even.append(string[i])
	else:
		odd.append(string[i])
for i in range(0,len(even)):
	outlist=outlist+even[i]+odd[i]
print(outlist)
