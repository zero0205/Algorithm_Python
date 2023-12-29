from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

s, t = map(int, input().split())

# dijkstra
dist = [int(1e9)] * (n+1)
dist[s] = 0
q = [(0, s)]
while q:
    d, now = heappop(q)
    for nx, nd in edges[now]:
        if d+nd < dist[nx]:
            dist[nx] = d+nd
            heappush(q, (d+nd, nx))
print(dist[t])
