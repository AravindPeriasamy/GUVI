x = list(input())
temp = []
for i in x:
	if i not in temp:
		temp.append(i)
temp.reverse()
output = "".join(temp)
print(output)
