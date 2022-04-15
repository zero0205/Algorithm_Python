# https://www.acmicpc.net/problem/12865

# # 그리디 -> 불가능(Fraction knapsack일때 가능)
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
# # DP (Knapsack)
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# weight = []
# value = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     weight.append(w)
#     value.append(v)

# dp = [[0] * (k + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         if weight[i-1] <= j:  # 현재 수용 가능한 가방의 무게를 넘지 않는다면
#             dp[i][j] = max(value[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]
                       
# print(dp[n][k])

##################
# 백트래킹
n, k = map(int, input().split())
goods = []
max_value = 0
max_profit = 0
for _ in range(n):
    w, v = map(int, input().split())
    goods.append((v/w, w, v))
    max_value = max(max_value, v)

goods.sort()    # 가성비 오름차순 정렬

def dfs(idx, w, v):
    global max_profit
    # 인덱스 범위 넘음
    if idx < 0:
        max_profit = max(v, max_profit)
        return
    ratio, nw, nv = goods[idx]
    # 가용 무게 넘음 or 더 진행해도 max 못 넘음
    if (w + nw) > k or (v + (idx + 1) * max_value) < max_profit:
        max_profit = max(v, max_profit)
        return
    # 이번 인덱스의 물건 포함
    dfs(idx - 1, w + nw, v + nv)
    # 이번 인덱스 물건 포함 X
    dfs(idx - 1, w, v)
    
dfs(n-1, 0, 0)
print(max_profit)