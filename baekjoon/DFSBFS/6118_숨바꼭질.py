from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS
q = deque([1])
dist = [int(1e9)]*(n+1)
dist[1] = 0
ans = [-1, -1, -1]
while q:
    now = q.popleft()
    for nx in graph[now]:
        if dist[nx] > dist[now]+1:
            q.append(nx)
            dist[nx] = dist[now]+1
            if ans[1] < dist[nx]:   # 더 먼 헛간 발견
                ans = [nx, dist[nx], 1]
            elif ans[1] == dist[nx]:    # ans와 같은 거리 헛간 발견
                if ans[0] > nx:
                    ans[0] = nx
                ans[2] += 1
print(*ans)
