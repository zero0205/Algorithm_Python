from collections import deque

s = int(input())
dp = [[int(1e9)]*(s+1) for _ in range(s+1)]

q = deque([(1, 0)])
dp[1][0] = 0
while q:
    screen, clip = q.popleft()
    t = dp[screen][clip]
    for ns, nc in [(screen, screen), (screen+clip, clip), (screen-1, clip)]:
        if 0 <= ns < s+1 and dp[ns][nc] > t+1:
            dp[ns][nc] = t+1
            q.append((ns, nc))
print(min(dp[s]))
