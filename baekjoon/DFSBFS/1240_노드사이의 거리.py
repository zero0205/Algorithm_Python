from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))


def bfs(start, end):
    q = deque([(start, 0)])
    visited = [False] * (n+1)
    visited[start] = True

    while q:
        now, dist = q.popleft()
        if now == end:
            return dist
        for nx, cost in graph[now]:
            if not visited[nx]:
                q.append((nx, dist+cost))
                visited[nx] = True


for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))
