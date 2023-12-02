n = int(input())
dp = [[0]*3 for _ in range(n)]
dp[0][0] = 1  # 사자 배치 X
dp[0][1] = 1  # 0열에 사자 배치
dp[0][2] = 1  # 1열에 사자 배치

for i in range(1, n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

ans = (dp[n-1][0] + dp[n-1][1] + dp[n-1][2]) % 9901
print(ans)
