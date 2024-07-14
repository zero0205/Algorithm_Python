n = int(input())


def solution(n):
    total = n*(n+1)//2
    if total % 2 == 1:
        return 0
    dp = [[0]*(total//2+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, total//2+1):
            dp[i][j] = dp[i-1][j]
            if j-i >= 0:
                dp[i][j] += dp[i-1][j-i]
    return dp[n][total//2]//2


print(solution(n))
