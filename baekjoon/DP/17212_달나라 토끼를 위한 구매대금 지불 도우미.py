n = int(input())

dp = [int(1e9)]*(n+1)   # dp[i]: i원 만드는 데 필요한 동전의 최소 개수
dp[0] = 0
for i in range(1, n+1):
    for j in [1, 2, 5, 7]:
        if i-j < 0:
            break
        else:
            dp[i] = min(dp[i], dp[i-j]+1)
print(dp[n])
