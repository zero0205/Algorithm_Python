import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
orders = []
for _ in range(n):
    x, y = map(int, input().split())
    orders.append((x, y))

dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
answer = 0
for order_idx in range(1, n+1):
    now_burger, now_fry = orders[order_idx-1]
    for burger in range(m+1):
        for fry in range(k+1):
            if burger+now_burger <= m and fry+now_fry <= k:
                dp[order_idx][burger][fry] = max(
                    dp[order_idx-1][burger+now_burger][fry+now_fry]+1, dp[order_idx-1][burger][fry])
            else:
                dp[order_idx][burger][fry] = dp[order_idx-1][burger][fry]
            if answer < dp[order_idx][burger][fry]:
                answer = dp[order_idx][burger][fry]
print(answer)
