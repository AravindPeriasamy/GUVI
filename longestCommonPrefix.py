n = int(input())
success = True
string = ""
final = ""
list1 = [input() for e in range(n)]
minimum = min(list1, key = len)
for i in range(0,len(minimum)):
	string +=minimum[i]
	for j in range(0,len(list1)):
		if  not list1[j].startswith(string):
			success = False
	if success == False:
		break
	else:
		final += minimum[i]
print(final)
