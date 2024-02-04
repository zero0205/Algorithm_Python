n, m = map(int, input().split())
fuels = [list(map(int, input().split())) for _ in range(n)]

dp = [[[int(1e9)]*3 for _ in range(m)] for _ in range(n+1)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = 0

for i in range(1, n+1):
    for j in range(m):
        if j == 0:
            dp[i][j][1] = dp[i-1][j][2]+fuels[i-1][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1])+fuels[i-1][j]
        elif 0 < j < m-1:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2])+fuels[i-1][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2])+fuels[i-1][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1])+fuels[i-1][j]
        else:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2])+fuels[i-1][j]
            dp[i][j][1] = dp[i-1][j][0]+fuels[i-1][j]
ans = int(1e9)
for j in range(m):
    ans = min(min(dp[n][j]), ans)
print(ans)
