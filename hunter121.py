x = list(input())
length = 1
for i in range(len(x)-1):
	for j in range(i+1,len(x)):
		string = x[i:(j+1)]
		if string == string[::-1]:
			if len(string) > length:
				length = len(string)
				output ="".join(string)
print(output)
