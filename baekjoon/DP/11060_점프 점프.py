n = int(input())
arr = list(map(int, input().split()))

dp = [1001] * n
dp[0] = 0
for i in range(n):
    for j in range(1, arr[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i]+1, dp[i+j])
print(dp[n-1] if dp[n-1] != 1001 else -1)

# from collections import deque

# n = int(input())
# arr = list(map(int, input().split()))

# visited = [False] * n
# q = deque([(0, 0)])
# visited[0] = True
# while q:
#     now, cnt = q.popleft()
#     if now == n-1:
#         print(cnt)
#         exit()
#     for i in range(1, arr[now]+1):
#         if now+i < n and not visited[now+i]:
#             q.append((now+i, cnt+1))
#             visited[now+i] = True
# print(-1)
