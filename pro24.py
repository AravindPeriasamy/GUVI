def printing(outlist,x):
	for i in range(x):
		print(outlist[i],end="")
	print()
def combinations(x,outlist,counter):
	if counter == x:
		printing(outlist,x)
		return
	outlist[counter] = 0
	combinations(x,outlist,counter+1)
	outlist[counter] = 1
	combinations(x,outlist,counter+1)
x = int(input())
outlist = [None]*x
combinations(x,outlist,0)