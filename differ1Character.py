count = 0
alp1, alp2= map(str,input().split(" "))
for i in range(0,len(alp1)):
	if alp1[i] != alp2[i]:
		count+=1
if count == 1:
	print("yes")
else:
	print("no")
