x = input()
list1 = [int(e) for e in input().split()]
list2 = [0]*(int(max(list1))+1)
for i in list1:
	list2[i] += 1
answer = list2.index(max(list2))
print(answer)
