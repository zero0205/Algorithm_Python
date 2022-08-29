######### DFS (시간 초과) ###########
# import sys
# input = sys.stdin.readline

# n = int(input())
# costs = [[] for _ in range(n+1)]
# for i in range(n):
#     r, g, b = map(int, input().split())
#     costs[i+1] = (sorted([(r,0),(g, 1),(b, 2)]))    # 0: red, 1: green, 2: blue

# min_cost = 1000001    
# color = [-1] * (n + 1)

# def dfs(num, cost):
#     global min_cost
    
#     for c, rgb in costs[num+1]:
#         if cost + c > min_cost:
#             continue
#         if num == 0:    # 1번 집
#             color[num+1] = rgb
#             dfs(1, c)
#             color[num+1] = 0
#         elif num == n - 1:  # n번 집
#             if rgb == color[1] or rgb == color[num]: 
#                 continue
#             else:
#                 min_cost = min(min_cost, cost + c)
#                 return
#         else:   # i번 집
#             if rgb == color[num]:
#                 continue
#             else:
#                 color[num+1] = rgb
#                 dfs(num+1, cost + c)
#                 color[num+1] = 0

# dfs(0, 0)
# print(min_cost)

############################################
import sys
input = sys.stdin.readline

n = int(input())
costs = []
min_cost = 1000001

for i in range(n):
    r, g, b = map(int, input().split())
    costs.append([r,g,b])    # 0: red, 1: green, 2: blue

for first in range(3):
    dp = [[1000001 for _ in range(3)] for _ in range(n)]
   
    dp[0][first] = costs[0][first]
    
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    for j in range(3):
        if j == first:
            continue
        else:
            min_cost = min(min_cost, dp[n-1][j])
            
print(min_cost)