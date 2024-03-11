n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in map(int, input().split()):
    if i in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
