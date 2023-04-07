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
total_cost = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(roads, (c, a, b))
    total_cost += c

min_cost, cnt = 0, 1  
while roads:
    c, a, b = heappop(roads)
    if find(a) != find(b):  # 사이클 형성하는지 체크
        union(a,b)
        min_cost += c
        cnt += 1
    if cnt == n:    # 모든 건물 연결 완료
        print(total_cost-min_cost)
        exit()
print(-1)