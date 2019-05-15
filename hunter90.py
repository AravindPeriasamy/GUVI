x = input()
x += "1"
i = 0
numbers = []
counts = []
output = ""
while i<len(x)-1:
	if x[i] == x[i+1]:
		count = 0
		for j in  range(i,(len(x)-1)):
			if x[j] == x[j+1]:
				count += 1
			else:
				count+=1
				j+=1
				break
		counts.append(count)
		numbers.append(x[i])
		i = j
	else:
		output += x[i]
		i += 1
answer = numbers[counts.index(max(counts))]
maximum = max(counts)
print(answer, maximum)
