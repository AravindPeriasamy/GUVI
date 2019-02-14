a = input()
string = ['d','h','o','n','i']
count = [0,0,0,0,0]
for i in a:
	if i in string:
		count[string.index(i)] += 1
for i in count:
	if i!=1:
		print("no")
		break
else:
	print("yes")
print(count)
