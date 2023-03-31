import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
# 진입 차수가 0인 노드들 큐에 넣기
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    print(now, end=' ')
    for nx in graph[now]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)