x, y, z = map(str,input().split(" "))
count = 0
for i in range(int(x),int(y)):
	if z in str(i):
		count += 1
print(count)
