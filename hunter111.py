n = int(input())
sum = 0
x = [ [int(e) for e in input().split()] for i in range(n)]
for i in range(n):
	sum += x[i][i]
print(sum)
