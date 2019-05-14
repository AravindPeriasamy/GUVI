x = int(input())
list1 =[str(n) for n in input().split()]
y = input()
count = 0
for i in  list1:
	if i.startswith(y):
		count += 1
print(count)
