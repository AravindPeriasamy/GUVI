a = input()
b = a
c = a
a=list(a)
c = list(c)
xlength = -1
ylength = -1
for i in range(0, len(a)):
	x = "".join(a)
	a.reverse()
	y = "".join(a)
	a.reverse()
	xlength += 1
	if x == y:
		break
	else:
		a.pop()
for i in range(0, len(c)):
	x = "".join(c)
	c.reverse()
	y = "".join(c)
	c.reverse()
	ylength += 1
	if x == y:
		break
	else:
		c.pop(0)
if ylength>=xlength:
	print(xlength)
else:
	print(ylength)
