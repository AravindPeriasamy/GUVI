a =input()
x = a.rstrip('0')
if x == x[::-1]:
	print("yes")
else:
	print("no")
