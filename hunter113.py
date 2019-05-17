n = int(input())
code = 0
if (n == 0): 
	print("NO")
else:
    while (n != 1): 
            if (n % 2 != 0): 
                code = 1
            n = n // 2
    if code == 0:
    	print("YES")
    else:
    	print("NO")
