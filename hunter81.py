x = int(input())
count = 1
for i in (range(1,(x+1))):
	if len(str(i)) == 1:
		count += 1
	else:
		temp = str(i)
		temp.split()
		spl = 0
		for j in range(0,(len(temp)-1)):
			if (abs(int(temp[j]) - int(temp[j+1])) == 1) or temp[j] == '0' and temp[j+1] == '9' or temp[j] == '9' and temp[j+1] == '0':
				spl = 1
		if spl == 1:
			count += 1
			spl = 0
print(count)
