from collections import deque

n = int(input())
times = [0]
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for i in range(n):
    t, *preceded, _ = list(map(int, input().split()))
    times.append(t)
    for building in preceded:
        graph[building].append(i+1)
    indegree[i+1] = len(preceded)

q = deque()
answer = [0]*(n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        answer[i] = times[i]

while q:
    now = q.popleft()
    for nx in graph[now]:
        indegree[nx] -= 1
        answer[nx] = max(answer[nx], answer[now]+times[nx])
        if indegree[nx] == 0:
            q.append(nx)

for i in range(1, n+1):
    print(answer[i])
