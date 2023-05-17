import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
task = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
spend_time = [0] * (n+1)
for i in range(1, n+1):
    time, num, *job = map(int, input().split())
    for j in job:
        task[j].append(i)   # j->i
    indegree[i] = num       # 진입차수
    spend_time[i] = time

# 위상정렬
q = deque()
ans = [0] * (n+1)
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = spend_time[i]

while q:
    now = q.popleft()
    for next in task[now]:
        indegree[next] -= 1
        ans[next] = max(ans[next], ans[now]+spend_time[next])
        if indegree[next] == 0: # 진입차수가 0이 되면 q에 삽입
            q.append(next)
 
print(ans[n])