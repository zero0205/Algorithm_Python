# https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
  for j in range(i + 1):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))