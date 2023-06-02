n, m = map(int, input().split())
INF = int(1e9)
fuel = []
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]
for i in range(n):
    fuel.append(list(map(int, input().split())))
    if i == 0:
        for j in range(m):
            for k in range(3):
                dp[0][j][k] = fuel[0][j]
        
for i in range(1, n):
    for j in range(m):
        for k in  range(3):
            if (j == 0 and k == 0) or (j == m-1 and k == 2):    # 불가능한 곳
                continue
            if k == 0:
                dp[i][j][k] = min(dp[i-1][j-1][1:]) + fuel[i][j]
            elif k == 1:
                dp[i][j][k] = min(dp[i-1][j][0], dp[i-1][j][2]) + fuel[i][j]
            else:
                dp[i][j][k] = min(dp[i-1][j+1][:2]) + fuel[i][j]
ans = int(1e9)
for i in range(m):
    ans = min(min(dp[n-1][i]), ans)
print(ans)