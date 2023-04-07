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

# 우주신들의 좌표        
pos = [[-1,-1]]
hq = []
for i in range(1, n+1):
    a, b = map(int, input().split())
    pos.append([a,b])
    for j in range(1, i):
        dist = ((a-pos[j][0])**2+(b-pos[j][1])**2) ** 0.5
        heappush(hq, (dist, i, j))
    
# 이미 연결된 통로
for _ in range(m):
    a, b = map(int, input().split())
    union(a,b)

ans = 0
while hq:
    c, a, b = heappop(hq)
    if find(a) != find(b):  # 사이클 형성하는지 체크
        union(a,b)
        ans += c

print("{:.2f}".format(ans))