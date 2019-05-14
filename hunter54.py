x = int(input())
list1 = list(map (int,input().split(" ")))
small = list1[0]
outlist = []
for i in list1:
	if small>i:
		small = i
	outlist.append(	small)
print(*outlist)
