row, col = (map(int,input().split(" ")))
l = [list(map(int,input().split(" "))) for i in range(row)]
for i in range(row):
	for j in range(col):
		if l[i][j] == 0:
			l[i][j] = 10000
for i in range(row):
	for j in range(col):
		if l[i][j] == 10000:
			for x in range(row):
				l[x][j] = 0
			for y in range(col):
				l[i][y] = 0
for i in range(row):
		print(*l[i])
