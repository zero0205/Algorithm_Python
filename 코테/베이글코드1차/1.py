# def solution(width, height, diagonals):
#     # 3차원 배열 / [행][열][대각선 이용 X, 이용 O]
#     dp = [[[0] * 2 for _ in range(width+1)] for _ in range(height+1)]

#     for i in range(width+1):
#         dp[0][i][0] = 1
#     for j in range(height+1):
#         dp[j][0][0] = 1

#     for i in range(1, height+1):
#         for j in range(1, width+1):
#             if i == 0 and j == 0:
#                 continue
#             dp[i][j][0] = (dp[i-1][j][0] + dp[i][j-1]) % 10000019
#             if [j, i] in diagonals:
#                 dp[i][j][1] = min(dp[i-1][j-1])

#     return dp[0][width][1]
import math

def solution(width, height, diagonals):
    answer = 0
    for x, y in diagonals:
        num1 = math.factorial(x-1+y) // (math.factorial(x-1) * math.factorial(y))
        num2 = math.factorial(width-(x-1)+height-y) // (math.factorial(width-(x-1)) * math.factorial(height-y))
        num3 = math.factorial(x+y-1) // (math.factorial(x) * math.factorial(y-1))
        num4 = math.factorial(width-x+height-(y-1)) // (math.factorial(width-x) * math.factorial(height-(y-1)))
        answer += (num1 * num2 + num3 * num4) % 10000019

    return answer

print(solution(2,2,[[1,1],[2,2]]))
print(solution(51,37,[[17,19]]))