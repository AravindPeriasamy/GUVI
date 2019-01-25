n = input()
count = 0
for i in n:
	if not i.isalnum()and i!=" ":
		count+=1
print(count)
