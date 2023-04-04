n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[j] == 0: # i와 j는 연결안됨
            continue
        # i와 j 연결됨
        i = find(i)
        j = find(j)
        if i == j:
            continue
        if i < j:
            parent[j] = i
        else:
            parent[i] = j
# 여행 계획
plan = list(map(int, input().split()))
city = find(plan[0]-1)
for p in plan[1:]:
    if find(p-1) != city:
        print("NO")
        exit()
print("YES")