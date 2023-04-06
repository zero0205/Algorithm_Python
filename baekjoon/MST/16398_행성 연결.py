import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

parent = [i for i in range(n+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
edges = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        heappush(edges, (arr[j], i, j))
    
ans, cnt = 0, 1
while edges:
    c, a, b = heappop(edges)
    if find(a) != find(b):  # 사이클을 만들지 않는다면 union
        union(a, b)
        ans += c
        cnt += 1
    if cnt == n:    # 제국 내 모든 행성 연결 완료
        break
print(ans)