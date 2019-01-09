n, m = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
sum = 0
for i in range(0,m):
	sum += numbers[i]
print(sum)
