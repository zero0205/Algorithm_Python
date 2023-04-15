n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[1][arr[1]] = 1
for i in range(2, n):
    for j in range(21):
        # 덧셈
        if j - arr[i] >= 0:
            dp[i][j] += dp[i-1][j-arr[i]]
        # 뺄셈
        if j + arr[i] <= 20:
            dp[i][j] += dp[i-1][j+arr[i]]
print(dp[n-1][arr[n]])