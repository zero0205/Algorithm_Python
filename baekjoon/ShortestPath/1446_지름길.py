n, d = map(int, input().split())
roads = []
for _ in range(n):
    s, e, l = map(int, input().split())
    roads.append((s, l, e))

roads.sort()

dp = [i for i in range(10001)]    # i번 위치까지 운전해야 하는 최소 거리
for i in range(n):
    s, l, e = roads[i]
    if dp[e] > dp[s] + l:
        dp[e] = dp[s] + l
        for j in range(1, d-e+1):
            dp[e+j] = min(dp[e] + j, dp[e+j])
print(dp[d])
