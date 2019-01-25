n = int(input())
outlist = []
numlist = list(map(int,input().split(" ")))
list1 = [0 for i in range(10)]
for i in range(0,len(numlist)):
	list1[numlist[i]] += 1
for i in range(0,len(list1)):
	if list1[i]>1:
		outlist.append(i)
if len(outlist) == 0:
	print("unique")
else:
	print(*outlist)
