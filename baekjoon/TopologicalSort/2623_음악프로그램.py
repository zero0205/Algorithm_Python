import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
order = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        order[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for nx in order[now]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)
            
if len(ans) == n:   # 순서 정하기 가능
    print(*ans, sep='\n')
else:   # 순서 정하기 불가능
    print(0)