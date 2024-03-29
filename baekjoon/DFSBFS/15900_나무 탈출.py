from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# BFS
q = deque([1])
dist = [int(1e9)]*(n+1)
dist[1] = 0
total = 0
while q:
    now = q.popleft()
    for nx in edges[now]:
        if dist[nx] > dist[now]+1:
            q.append(nx)
            dist[nx] = dist[now]+1
    if len(edges[now]) == 1 and now != 1:
        total += dist[now]


print("Yes" if total % 2 == 1 else "No")
