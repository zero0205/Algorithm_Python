import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
ans = 0
parent = [i for i in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) and ans == 0:
        ans = i + 1
    union_parent(parent, a, b)
    
print(ans)