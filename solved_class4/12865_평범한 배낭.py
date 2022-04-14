# https://www.acmicpc.net/problem/12865

# # 그리디
# import heapq

# n, k = map(int, input().split())
# goods = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     ratio = w / v
#     heapq.heappush(goods, (ratio, w, v))

# sum = 0
# while goods:
#     x = heapq.heappop(goods)
#     if k - w >= 0:
#         sum += v
#         k -= w
        
# print(sum)

####################
# DP (Knapsack)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight = []
value = []
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if weight[i-1] <= k:
            dp[i][j] = max(value[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
            
print(dp[n][k])

##################
# # 백트래킹
# n, k = map(int, input().split())
# weight = []
# value = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     weight.append(w)
#     value.append(v)