n = int(input())
p = list(map(int, input().split()))
m = int(input())

dp = ['0'] * (m+1)    # 금액별 가능한 최대 방 번호

for money in range(1, m+1):  # 금액
    for num in range(n):
        if money-p[num] >= 0:
            dp[money] = str(max(int(dp[money-p[num]])*10+num, int(dp[money])))

print(dp[m])