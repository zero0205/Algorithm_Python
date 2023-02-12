n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    if dp[i-1] <= 0:    # 앞의 연속된 수를 더해봤자 최대값을 만드는데에 손해 or 영향 X
        dp[i] = arr[i]
    else:               # 앞의 수를 더하는게 이득
        dp[i] = dp[i-1] + arr[i]

print(max(dp))