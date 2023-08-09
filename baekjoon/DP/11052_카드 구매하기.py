n =int(input())
price = [0] + [i for i in map(int, input().split())]
dp = [0] * (n+1)    # 카드를 n개 샀을 때의 최댓값

for i in range(1, n+1):
    for j in range(i, 0, -1):
        dp[i] = max(dp[i], dp[i-j]+price[j])
print(dp[n])