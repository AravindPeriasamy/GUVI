a,b = map(str,input().split(" "))
state = False
for i in range(0,len(a)-1):
	for j in range(2,len(a)):
		if a[i:j] in b:
			print("yes")
			state =True
			break
	if state == True:
		break
if state != True:
	print("no")
