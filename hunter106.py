x = list(input())
y = list(input())
out = ""
dif = abs(len(x) - len(y))
if dif == 0:
	temp =0
elif len(x) > len(y):
	for i in range(dif):
		y.append(" ")
else:
	for i in range(dif):
		x.append(" ")
for i in range(len(x)):
	out +=x[i] + y[i]
	print(out)
	out = ""
