n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
    
dp = [[0 for _ in range(3)] for _ in range(n)]  # 0열 안 마심, 1열 마심, 2열 연달아 2잔째
dp[0][0] = 0
dp[0][1] = wine[0]
if n > 1:
    for i in range(n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + wine[i]
        dp[i][2] = dp[i-1][1] + wine[i]
print(max(dp[-1]))