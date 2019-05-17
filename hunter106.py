x = list(input())
y = list(input())
out = ""
outlist = []
dif = abs(len(x) - len(y))
if dif == 0:
	temp =0
elif len(x) > len(y):
	for i in range(dif):
		y.append(" ")
else:
	for i in range(dif):
		x.append(" ")
for i in range(len(x)-1):
	out +=y[i] + x[i]
	outlist.append(out)
	out = ""
out += y[(len(x)-1)] + x[(len(x)-1)]
outlist.append(out)
for i in outlist:
	print(i)
