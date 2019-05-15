x, y = map(int , input().split())
string = input().split()
pos = "".join(string).rindex('*')
answer = (pos+1)//y
print(answer)
