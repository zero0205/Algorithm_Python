from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([(1, 0)])
visited = [False] * (n+1)
visited[1] = True
ans = 0
while q:
    now, cnt = q.popleft()
    if cnt == 2:    # 친구의 친구까지만 초대
        continue
    for nx in graph[now]:
        if not visited[nx]:
            q.append((nx, cnt+1))
            visited[nx] = True
            ans += 1
print(ans)
