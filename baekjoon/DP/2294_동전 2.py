n, k = map(int, input().split())
coin = set()
for _ in range(n):
    coin.add(int(input()))
    
dp = [int(1e9)] * (k+100001)
dp[0] = 0
for c in coin:
    for num in range(k+1):
        dp[num+c] = min(dp[num+c], dp[num]+1)
print(dp[k] if dp[k] != int(1e9) else -1)