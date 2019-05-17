x, y = map(str,input().split(" "))
x = list(x)
y = list(y)
dif = abs(len(x) - len(y))
num =1
output = ""
if dif == 0:
	temp =0
elif len(x) > len(y):
	for i in range(dif):
		y.append(str(num))
		num +=1
else:
	for i in range(dif):
		x.append(str(num))
		num += 1
for i in range(len(x)):
	output += x[i] + y[i]
print(output)
