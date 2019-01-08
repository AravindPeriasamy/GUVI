n1,n2 = map(str,input().split())
temp1 = []
for i in range(0,len(n1)):
	if n1[i] not in temp1:
		temp1.append(n1[i])
temp2 = []
for i in range(0,len(n2)):
	if n2[i] not in temp2:
		temp2.append(n2[i])
if len(temp1) == len(temp2):
	print("yes")
else:
	print("no")
