start, end = map(int,input().split(" "))
list1 = []
for n in range(start,end):
	sum = 0
	number = n
	while n>0:
		rem = n%10
		sum = sum +( rem*rem*rem )
		n = n// 10
	if number == sum:
		list1.append(sum)
print(*list1)
