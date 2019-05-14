list1 = list(map(str,input().split(" ")))
output = ""
if len((list1)) == 1:
	print(*list1)
else:
	for i in range(0,(len(list1)-1)):
		if list1[i] != "":
			output += (list1[i].strip()) + " "
	output += (list1[(len(list1)-1)].strip())
	print(output)
