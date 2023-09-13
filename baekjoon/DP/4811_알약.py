while True:
    n = int(input())
    if n == 0:
        break
    dp = [[0]*(n+1) for _ in range(n+1)]  # 행: W, 열: H
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0]
        for j in range(1, n+1):
            if j > i:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[n][n])
