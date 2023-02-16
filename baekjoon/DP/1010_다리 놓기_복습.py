for _ in range(int(input())):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    # n = 1일 때 
    for i in range(m+1):
        dp[1][i] = i    # n이 1이라면 m개의 다리로 가는 경우의 수는 m
    
    for i in range(2, n + 1):
        for j in range(i, m + 1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]

    print(dp[n][m])