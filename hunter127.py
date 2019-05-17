x, y = map(str,input().split())
max = 0
for i in range(len(y)-1):
	for j in range(len(y)):
		if y[i:(j+1)] in x:
			length = len(y[i:(j+1)])
			if length > max:
				max = length
				output = y[i:(j+1)]
print (output)
