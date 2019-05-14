x = int(input())
list1 = [int(n) for n in input().split()]
small = (list1.index(min(list1)))+1
max = (list1.index(max(list1)))+1
print(small,max)
