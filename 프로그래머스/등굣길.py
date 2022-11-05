def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]   
    for i in range(2, n+1):
        dp[i][1] = 1
    for i in range(2, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(2, m+1):
            if [i, j] not in puddles:  # 물에 잠긴 지역이 아니라면
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]

print(solution(4, 3, [[2, 2]]))