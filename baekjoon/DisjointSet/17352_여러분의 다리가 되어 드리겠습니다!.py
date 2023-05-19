import sys
input = sys.stdin.readline

def find_parent(n, parent):
    if n != parent[n]:
        parent[n] = find_parent(parent[n], parent)
    return parent[n]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    if a == b:  # 이미 같은 그래프에 속함
        return
    # 번호가 더 작은 쪽을 부모로
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [i for i in range(n+1)]
for _ in range(n-2):
    a, b = map(int, input().split())
    union_parent(a, b, parent)
    
for i in range(2, n+1):
    if find_parent(i, parent) != 1:
        print(1, i)
        break