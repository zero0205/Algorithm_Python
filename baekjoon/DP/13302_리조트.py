n, m = map(int, input().split())
visit = [True] * (n+2)
if m > 0:
    for d in list(map(int, input().split())):
        visit[d] = False

dp = [[1001]*50 for _ in range(n+6)]   # 행: 날짜, 열: 쿠폰 수
dp[0][0] = 0

for i in range(n+1):
    for j in range(40):
        if dp[i][j] == 1001:
            continue
        if not visit[i+1]:  # 내일은 안 가는 날
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            continue
        if j >= 3:  # 쿠폰 사용
            dp[i+1][j-3] = min(dp[i][j], dp[i+1][j-3])
        # 1일권
        dp[i+1][j] = min(dp[i][j]+10, dp[i+1][j])
        # 3일권
        for k in range(1, 4):
            dp[i+k][j+1] = min(dp[i+k][j+1], dp[i][j]+25)
        # 5일권
        for k in range(1, 6):
            dp[i+k][j+2] = min(dp[i+k][j+2], dp[i][j]+37)
print(min(dp[n])*1000)
