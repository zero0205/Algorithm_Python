import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    if a == b:
        return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

n, m = map(int, input().split())
parent = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if not union_parent(a, b, parent):
        print(i+1)
        exit()
print(0)