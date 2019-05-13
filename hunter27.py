x = list(input())
output = ""
for i in range(len(x)):
	if x != x[::-1]:
		output = "".join(x)
		break
	x.pop()
print(output)
