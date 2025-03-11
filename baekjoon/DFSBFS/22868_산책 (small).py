from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
s, e = map(int, input().split())


def bfs(excludes):
    q = deque([[s]])
    visited = [False]*(n+1)
    for ex in excludes:
        visited[ex] = True
    visited[s] = True
    while q:
        now_path = q.popleft()
        for nx in graph[now_path[-1]]:
            if not visited[nx]:
                if nx == e:
                    return now_path
                q.append(now_path+[nx])
                visited[nx] = True


# S -> E
se_path = bfs([])
# E -> S
es_path = bfs(se_path[1:])
print(len(se_path)+len(es_path))
