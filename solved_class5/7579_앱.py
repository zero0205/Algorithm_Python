# n, m = map(int, input().split())
# byte = list(map(int, input().split()))
# cost = list(map(int, input().split()))

# min_cost = int(1e9)
# acc = [byte[-1]]

# for i in range(1, n):
#     acc.append(acc[i-1] + byte[n-i-1])

# def knapsack(idx, total_cost, total_byte):
#     global min_cost
#     if total_byte > m:
#         min_cost = min(min_cost, total_cost)
#         return
#     if promising(total_byte, total_cost, idx):
#         knapsack(idx+1, total_cost + cost[idx+1], total_byte + byte[idx+1])
#         knapsack(idx+1, total_cost, total_byte)
        
# def promising(total_byte, total_cost, idx):
#     global min_cost
#     if idx == n - 1:
#         return False
#     if total_cost > min_cost:  
#         return False    
#     if total_byte + acc[n-idx-1] < m:    
#         return False
#     return True
    
# knapsack(0, 0, 0)
# print(min_cost)

########################################################
n, m = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

sum_cost = sum(cost)

# 행이 앱의 인덱스, 열이 비용, 배열의 값은 그때의 최대 메모리
dp = [[0 for _ in range(sum_cost + 1)] for _ in range(n + 1)]

min_cost = 10001

for i in range(1, n + 1):
    for j in range(sum_cost + 1):
        if cost[i-1] > j: # 비용이 충분치 않아서 앱 종료 X
            dp[i][j] = dp[i-1][j]
        else:   # 앱 종료 가능
            dp[i][j] = max(dp[i-1][j-cost[i-1]] + byte[i-1], dp[i-1][j])
        # 이번에 구한 최대 메모리가 조건을 만족하는지 확인
        if dp[i][j] >= m:
            min_cost = min(min_cost, j)
            
print(min_cost)