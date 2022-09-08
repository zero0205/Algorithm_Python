from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())    # a < b
    graph[a].append(b)
    indegree[b] += 1
    
q = deque()    
# 진입차수가 0인 노드들을 큐에 삽입
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    now = q.popleft()
    print(now, end=" ")

    for nx in graph[now]:
        indegree[nx] -= 1
        if indegree[nx] == 0:   # 진입차수가 0이라면 큐에 삽입
            q.append(nx)
        