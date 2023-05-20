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
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(int(input())):
    n = int(input())    # 유저 수
    parent = [i for i in range(n)]
    
    for _ in range(int(input())):
        a, b = map(int, input().split())    # a와 b가 친구
        union_parent(a, b, parent)
        
    print("Scenario " + str(i+1) + ":")    
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if find_parent(u, parent) == find_parent(v, parent):
            print(1)
        else:
            print(0)
    print()