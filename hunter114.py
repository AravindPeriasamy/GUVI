def prime(n):
	i=2
	count = 0
	if n == 1:
		return False
	while i<=n:
		if n%i==0:
			count+=1
		i+=1
	if count <= 1:
		return True
	else:
		return False

def sumOfDigits(n):
	sum = 0
	n = list(str(n))
	for i in n:
		sum += int(i)
	return sum

start ,end = map(int,input().split(" "))
list1 = []
for i in range(start,end):
	list1.append(sumOfDigits(i))
count = 0
for i in list1:
	if (prime(i)):
		count += 1
print(count)
