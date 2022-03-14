# https://www.acmicpc.net/problem/2606

import sys
from collections import deque
from unittest import result

input = sys.stdin.readline

def bfs(graph):
    q = deque([1])
    result = 0
    visited = [False] * (n + 1)
    visited[1] = True
    while q:
        nx = q.pop()
        for node in graph[nx]:
            if not visited[node]:
                result += 1
                q.append(node)  
                visited[node] = True
    return result

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(bfs(graph))