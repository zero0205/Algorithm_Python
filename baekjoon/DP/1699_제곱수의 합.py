from math import sqrt

n = int(input())
dp = [int(1e6)] * 100_001
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, int(sqrt(i))+1):
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1
print(dp[n])
