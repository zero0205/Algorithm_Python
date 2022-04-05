# https://www.acmicpc.net/problem/1149

INF = int(1e9)
n = int(input())
price = []
dp = [[INF, INF, INF] for _ in range(n)]

for _ in range(n):
    price.append(list(map(int, input().split())))
    
dp[0] = price[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]
    
print(min(dp[n-1]))