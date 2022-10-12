# def solution(triangle):
#     answer = 0
#     n = len(triangle)
#     dp = [[0 for _ in range(n)] for _ in range(n)]
#     dp[0][0] = triangle[0][0]
#     for i in range(1, n):   # 행
#         for j in range(i):  # 열
#             if j == 0:
#                 dp[i][j] = dp[i-1][j] + triangle[i][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
#     return max(dp[-1])

def solution(triangle):
    n = len(triangle)
    for i in range(n-2, -1, -1):   # 행
        for j in range(i+1):  # 열
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))