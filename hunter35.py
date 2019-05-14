x = input()
if (len(x)%2 == 1):
	first = x[0:((len(x)//2))]
	last = x[((len(x)//2)+1):]
	if first == last:
		print("YES")
	else:
		print("NO")
else:
	print("NO")
