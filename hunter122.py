x = int(input())
code = 0
list1 = [int(x) for x in input().split()]
for i in range(1,x-1):
	prev = sum(list1[:i])
	next = sum(list1[i+1:])
	if prev == next:
		print("yes")
		code = 1
		break
if code == 0:
	print("no")
