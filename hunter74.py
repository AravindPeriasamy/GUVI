x = input()
y = input()
length = 0
maxx = 0
maxy = 0
for i in range((len(y)-1)):
	for j in range(i,len(y)):
		if y[i:j+1] in x:
			temp = y[i:j+1]
			if len(temp) >= int(length):
				length = len(y[i:j+1])
				maxx = i
				maxy = j
answer = y[maxx:maxy+1]
print(answer)
