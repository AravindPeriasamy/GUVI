a = input()
string = ['d','h','o','n','i']
count = [0,0,0,0,0]
exit = False
for i in a:
	if i in string:
		count[string.index(i)] += 1
	if i not in string:
		print("no")
		exit = True
for i in count:
	if i!=1 and exit!=True:
		print("no")
		break
else:
	if exit!=True:
		print("yes")
