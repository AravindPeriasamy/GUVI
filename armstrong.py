n = int(input())
number = n
sum = 0
while n>0:
	rem = n%10
	sum = sum +( rem*rem*rem )
	n = n// 10
print("yes" if sum == number else "no")
