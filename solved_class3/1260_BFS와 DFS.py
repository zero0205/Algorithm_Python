# https://www.acmicpc.net/problem/1260

# DFS
from collections import deque


def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")
    for node in graph[v]:
        if not visited[node]:
            dfs(node, visited)
    return

# BFS


def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        x = q.popleft()
        print(x, end=" ")
        for node in graph[x]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


# n: 정점의 개수, m: 간선의 개수, v: 시작 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우 번호가 작은 것부터 방문하기 위해 정렬
for lst in graph:
    lst.sort()

visited = [False] * (n + 1)
dfs(v, visited)
print()
bfs(v)
