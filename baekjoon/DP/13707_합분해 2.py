n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]  # j개의 수로 i를 만드는 방법의 수
for i in range(n+1):
    dp[i][1] = 1    # 1개의 수로 i를 만드는 방법은 1개
for j in range(1, k+1):
    dp[0][j] = 1    # j개의 수로 0을 만드는 방법은 1개
for i in range(1, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 1_000_000_000
print(dp[n][k])
