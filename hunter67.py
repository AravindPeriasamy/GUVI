list1 = [str(n) for n in input().split("#")]
list2 = [str(n) for n in input().split("#")]
total1 = int(list1[1])+int(list1[2])+int(list1[3])
total2 = int(list2[1])+int(list2[2])+int(list2[3])
if total1 >total2:
	print(list1[0])
else:
	print(list2[0])
