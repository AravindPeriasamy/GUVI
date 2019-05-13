x = list(input())
list1 = []
max =0
for i in range(len(x)):
	for j in range(i,len(x)):
		if x[j] not in list1:
			list1.append(x[j])
		else:
			if max< len(list1):
				max = len(list1)
			list1 = []
print(max)
