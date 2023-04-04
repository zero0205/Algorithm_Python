import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
        
# 루트 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:    # 집합 합치기
        union(a, b)
    else:           # 같은 집합인지 확인
        print("YES" if find(a) == find(b) else "NO")