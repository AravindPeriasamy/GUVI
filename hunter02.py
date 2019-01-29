num=int(input())
list1 = list(map(int, input().split(" ")))
list1.sort(reverse = True)
string = ""
for i in list1:
	string+= str(i)
print(int(string))
