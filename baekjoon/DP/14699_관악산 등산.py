from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
dp = [1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    if heights[a] > heights[b]:
        graph[a].append(b)
    elif heights[a] < heights[b]:
        graph[b].append(a)

for i in range(1, n+1):
    q = deque([(i, 1)])

    while q:
        now, cnt = q.popleft()
        for nx in graph[now]:
            if dp[nx] < cnt+1:
                q.append((nx, cnt+1))
                dp[nx] = cnt+1

for i in range(1, n+1):
    print(dp[i])
