x = list(input())
y= x.copy()
code = 0
for i in  range(len(x)):
	y.pop(i)
	if y == y[::-1]:
		code = 1
	y= x.copy()
if code == 1:
	print("YES")
else:
	print("NO")
