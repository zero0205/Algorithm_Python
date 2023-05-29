n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
    
dp = [0] * (k+100001)
dp[0] = 1
for c in coin:
    for i in range(k+1):
        dp[i+c] += dp[i]
print(dp[k])