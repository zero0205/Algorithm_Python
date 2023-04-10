n = int(input())
dp = [[0] * 10 for _ in range(n+1)] # 길이가 i일 때 마지막 숫자가 j인 계단 수의 개수
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n]) % 1_000_000_000)