import sys
input = sys.stdin.readline


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    if a == b:  # 사이클 형성
        return False
    
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
    return True
    

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
disconnect = 0
for _ in range(m):
    u, v = map(int, input().split())
    if not union_parent(u, v, parent):
        disconnect += 1

for i in range(1, n+1):
    parent[i] = find_parent(i, parent)

parent_set = set(parent[1:])
print(len(parent_set)-1+disconnect)
