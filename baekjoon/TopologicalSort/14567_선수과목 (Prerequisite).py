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
    
ans = [0] * (n+1)
semester = [0] * (n+1)

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:    # 진입차수가 0인 노드들 큐에 삽입
        q.append((i, 1))
        semester[i] = 1   # 1학기에 수강 가능한 과목들

while q:
    subject, cnt = q.popleft()
    if graph[subject]:
        for next_node in graph[subject]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:    # 진입차수가 0이 되면 큐에 삽입
                q.append((next_node, cnt + 1))
                semester[next_node] = cnt + 1
print(*semester[1:n+1])