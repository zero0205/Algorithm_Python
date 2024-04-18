from collections import deque

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())    # a가 b보다 잘함
    graph[a].append((b, 1))
    graph[b].append((a, -1))


def bfs(start, dir):
    res = 0
    q = deque([start])
    visited = [False]*(n+1)
    visited[start] = True
    while q:
        now = q.popleft()
        for nx, d in graph[now]:
            if not visited[nx] and d == dir:
                q.append(nx)
                visited[nx] = True
                res += 1
    return res


high = bfs(x, -1)+1
low = bfs(x, 1)
print(high, n-low)
