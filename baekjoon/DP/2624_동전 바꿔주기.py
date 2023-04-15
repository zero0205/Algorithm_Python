t = int(input())    # 지폐 금액
k = int(input())    # 동전 가지 수
coins = [[0, 0]]
for _ in range(k):
    coins.append(list(map(int, input().split())))
dp = [[0] * (t+1) for _ in range(k+1)]  # 행은 코인 인덱스, 열은 금액
dp[0][0] = 1
for i in range(1, k+1): # 동전 인덱스
    p, n = coins[i]
    for money in range(t+1):   # 금액
        dp[i][money] = dp[i-1][money]
        for j in range(1, n+1):     # 코인 개수
            if money-p*j >= 0:
                dp[i][money] += dp[i-1][money-p*j]
            else:
                break
print(dp[k][t])