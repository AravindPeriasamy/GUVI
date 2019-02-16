b = int(input())
list1 = [int(i) for i in input().split()]
list1.sort()
increment = 1
candies = 0
list1.insert(0,list1[0])
for i in range(1,len(list1)):
	if list1[i]>list1[i-1]:
		increment += 1
	candies += increment
print(int(candies))
