x=list(input())
sum = 0
for i in x:
	sum += int(i)
y = str(sum)
if y == y[::-1]:
	print("YES")
else:
	print("NO")
