a = int(input())
list1 = [int(i) for i in input().split()]
list1.sort(reverse = True)
sum = list1[0] + list1[1]
print(sum)
