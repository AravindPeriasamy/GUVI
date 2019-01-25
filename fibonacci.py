a=0
b=1
list1=[]
n= int(int(input()))
print( b ,end = '\t')
for i in range(2,n+1):
	c=a+b
	a=b
	b=c
	list1.append(c)
print(*list1)
