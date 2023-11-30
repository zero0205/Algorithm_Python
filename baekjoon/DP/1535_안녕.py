n = int(input())
loss = [0] + list(map(int, input().split()))
joy = [0] + list(map(int, input().split()))

dp = [[0]*101 for _ in range(n+1)]  # i번 사람에게 인사하고 남은 체력이 j일 때의 기쁨
for i in range(1, n+1):
    for j in range(101):
        dp[i][j] = dp[i-1][j]
        if j + loss[i] < 101:
            dp[i][j] = max(dp[i-1][j+loss[i]] + joy[i], dp[i][j])
ans = 0
for j in range(1, 101):
    ans = max(ans, dp[n][j])
print(ans)
