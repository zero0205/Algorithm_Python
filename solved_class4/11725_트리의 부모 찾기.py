# https://www.acmicpc.net/problem/11725

from collections import deque

def bfs(n):
    q = deque([1])
    visited = [False] * (n + 1)
    parent = [i for i in range(n + 1)]
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                parent[node] = now
                q.append(node)
    return parent

n = int(input())
graph = [[] for _ in range(n + 1)]

# def dfs(v, visited):
#     visited[v] = True
#     for node in graph[v]:
#         if not visited[node]:
#             parent[node] = v
#             dfs(node, visited)
#     return
            
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)
parent = bfs(n)
# dfs(1, visited)
for p in parent[2:]:
    print(p)