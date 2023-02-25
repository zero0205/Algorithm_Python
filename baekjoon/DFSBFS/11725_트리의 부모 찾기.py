from collections import deque

n = int(input())
connect = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False] * (n+1)
visited[1] = True
q = deque([1])
while q:
    now = q.popleft()
    for nx in connect[now]:
        if not visited[nx]:
            parent[nx] = now
            q.append(nx)
            visited[nx] = True
            
for i in range(2, n+1):
    print(parent[i])