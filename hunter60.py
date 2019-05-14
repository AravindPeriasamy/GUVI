x = int(input())
list1 = list(map (int,input().split(" ")))
list2 = list(map (int,input().split(" ")))
count = 1
while(1):
	temp=list1.pop(0)
	list1.append(temp)
	if list1 == list2:
		print(count)
		break
	else:
		count +=1
