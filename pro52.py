a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))
d = list(map(int,input().split(" ")))
outlist = []
for i in a:
	if i not in outlist:
		outlist.append(i)
for i in b:
	if i not in outlist:
		outlist.append(i)
for i in c:
	if i not in outlist:
		outlist.append(i)
for i in d:
	if i not in outlist:
		outlist.append(i)
if len(outlist)%2 == 0:
	print("yes")
else:
	print("no")
