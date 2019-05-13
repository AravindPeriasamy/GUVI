def printing(outlist,x):
	out = ""
	global output
	for i in range(x):
		#print(outlist[i],end="")
		out +=str(outlist[i])
	output.append(out)
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
output =[]
combinations(x,outlist,0)
for i in output:
	print(i)
