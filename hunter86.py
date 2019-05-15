x = int(input())
count = 0
for i in range(x+1):
	count += str(i).count('2')
print(count)
