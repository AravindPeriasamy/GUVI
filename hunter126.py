x = [str(i) for i in input().split()]
code = 0
for i in x:
	if (i[0].islower() == True):
		code = 1
if code == 0:
	print("yes")
else:
	print("no")
