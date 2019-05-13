x = int(input())
out = 0
l = list(map(int,input().split(" ")))
for i in range(x-1):
	first = (sum(l[0:(i+1)]))//(i+1)
	last = ((sum(l[(i+1):(x+1)])))//(x-(i+1))
	if(first == last):
		out = 1
if out==1:
	print("yes")
else:
	print("no")
