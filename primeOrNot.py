n=int(input())
i=2
count = 0
while i<=n:
	if n%i==0:
		count+=1
	i+=1
if count <= 1:
	print("yes")
else:
	print("no")
