n = int(input())
x = list(map(int,input().split(" ")))
superstar = max(x)
star = []
x.append(0)
x.append(0)
x.insert(0,0)
for i in range(1,len(x)-1):
	if x[i] > max(x[(i+1):]):
		star.append(x[i])
print(*star)
print(superstar)
