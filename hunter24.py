a,b = map(int,input().split(" "))
flag = False
list1 = list(map(int,input().split(" ")))
for i in range(0,(a-1)):
	for j in range((i+1),a):
		if list1[i] + list1[j] == b:
			print("YES")
			flag = True
			break
	if flag == True:
			break
if flag == False:
	print("NO")
