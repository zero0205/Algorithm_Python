import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from collections import deque

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
s, e = map(int, input().split())
edges = []
for _ in range(m):
    h1, h2, k = map(int, input().split())
    heappush(edges, (-k, h1, h2))
    
# MST 형성
mst = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
while edges:
    w, a, b = heappop(edges)
    if union_parent(a, b, parent):
        mst[a].append((-w, b))
        mst[b].append((-w, a))


# BFS로 s->e 찾아가며 간선의 최소치 기록
ans = int(1e6)
q = deque([(s, int(1e9))])
visited = [False] * (n+1)
visited[s] = True
while q:
    now, min_v = q.popleft()
    if now == e:
        print(min_v)
        exit()
    for w, nx in mst[now]:
        if not visited[nx]:
            q.append((nx, min(min_v, w)))
            visited[nx] = True
            
print(0)    # 연결되어 있지 않아서 전달할 수 없는 경우