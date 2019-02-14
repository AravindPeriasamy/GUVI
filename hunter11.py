n = input().split(" ")
output = []
for i in n:
	output.append(i[::-1])
print(*output)
