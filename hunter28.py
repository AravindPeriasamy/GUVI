x = list(input())
y = []
output = ""
for i in x:
	if i not in y:
		y.append(i)
for i in y:
	output +=i
print(output)
