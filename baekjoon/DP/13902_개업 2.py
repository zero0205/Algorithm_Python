import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
s = list(map(int, input().split()))

wok_set = set(s)
dp = [INF]*(n+1)
for i in range(m):
    dp[s[i]] = 1
    for j in range(i+1, m):
        if s[i]+s[j] <= n:
            wok_set.add(s[i]+s[j])
            dp[s[i]+s[j]] = 1

for i in range(1, n+1):
    if dp[i] == 1:
        continue
    for ws in wok_set:
        if i-ws < 0 or dp[i-ws] == INF:
            continue
        dp[i] = min(dp[i], dp[i-ws]+1)

print(dp[n] if dp[n] != INF else -1)
