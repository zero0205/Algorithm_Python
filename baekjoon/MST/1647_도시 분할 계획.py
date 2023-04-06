import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split())

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
        
roads = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(roads, (c, a, b))
    
ans, cnt = 0, 1
while roads:
    c, a, b = heappop(roads)
    if find(a) != find(b):  # 사이클을 만들지 않는다면 union
        union(a, b)
        ans += c
        cnt += 1
    if cnt == n-1:    # 2개 마을로 분리하며 각 마을별로 집 연결 완료
        break
print(ans)