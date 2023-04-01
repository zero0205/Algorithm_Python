import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
for i in range(1, n+1):
    sorted(graph[i])
    if indegree[i] == 0:
        heappush(q, i)
while q:
    now = heappop(q)
    print(now, end=' ')
    for nx in graph[now]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heappush(q, nx)