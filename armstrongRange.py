start, end = map(int,input().split(" "))
for n in range(start,end):
	sum = 0
	number = n
	while n>0:
		rem = n%10
		sum = sum +( rem*rem*rem )
		n = n// 10
	if number == sum:
		print(sum, end='\t')
