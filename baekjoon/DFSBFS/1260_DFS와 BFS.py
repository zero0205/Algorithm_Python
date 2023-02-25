from collections import deque

def dfs(v, visited):
    print(v,end=' ')
    visited[v] = True
    for nx in connect[v]:
        if not visited[nx]:
            dfs(nx, visited)

def bfs(v):
    visited = [False] * (n+1)
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nx in connect[now]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
    
n, m, v = map(int, input().split())
connect = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

for i in range(n+1):
    connect[i].sort()

visited = [False] * (n+1)
dfs(v, visited)
print()
bfs(v)