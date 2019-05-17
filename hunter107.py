x = list(input())
count = 1
for i in range(len(x)-1):
	for j in range(i+1,len(x)):
		z = x[i:(j+1)]
		if z == z[::-1]:
			length =len(x[i:(j+1)])
			if length>count:
				count = length
print(count)
