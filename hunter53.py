x = list(map (str,input().split(" ")))
outlist = []
word = x[0]
for i in range(((len(x[0])-int(x[1])))+1):
	outlist.append(word[i:(i+(int(x[1])))])
print(*outlist)
