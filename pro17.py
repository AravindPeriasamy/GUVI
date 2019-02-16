a, b = map(int,input().split(" "))
yes = "yes"
no = "no"
flag = False
list1 = [int(i) for i in input().split()]
for i in range((len(list1)-1)):
	for j in range(len(list1)):
		if list1[i]+list1[j] == b:
			print(yes)
			flag = True
			break
	if flag == True:
		break
if flag == False:
	print(no)
