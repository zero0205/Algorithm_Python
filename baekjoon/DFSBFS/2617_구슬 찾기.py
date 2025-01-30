from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
bigger = [[] for _ in range(n+1)]
smaller = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    bigger[b].append(a)
    smaller[a].append(b)


def bfs(start, graph):
    cnt = 0
    visited = [False]*(n+1)
    q = deque([start])
    while q:
        now = q.popleft()
        for nx in graph[now]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                cnt += 1
    return cnt


answer = 0
for i in range(1, n+1):
    if bfs(i, bigger) > n//2 or bfs(i, smaller) > n//2:
        answer += 1
print(answer)
