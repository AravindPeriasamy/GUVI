x, y = map(int , input().split())
string = input().split()
answer = 0
pos = "".join(string).rindex('*')
for i in  range(len(string)):
	answer +=1
	if pos <= y:
		break
	else:
		y += y
print(answer)
