n = int(input())
arr = [int(input()) for _ in range(n)]

# LIS
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
