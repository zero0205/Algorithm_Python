import sys
input = sys.stdin.readline

c, n = map(int, input().split())
info = []
dp = [int(1e9)] * (c+101)    # 고객 수별 최소 비용 저장
dp[0] = 0
for _ in range(n):
    info.append(list(map(int, input().split())))    # 비용, 고객 수
        
for cost, num in info:
    for i in range(num, c+101):
        dp[i] = min(dp[i], dp[i-num]+cost)
        
print(min(dp[c:]))