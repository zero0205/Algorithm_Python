########### PyPy3로만 통과 가능 ############
########## Python으로는 시간 초과 ##########
# import math

# n = int(input())

# dp = [5] * 50001
# dp[0] = 0

# for i in range(1, n+1):
#     for j in range(int(math.sqrt(i)), 0, -1):
#         if dp[i] == 1:
#             break
#         dp[i] = min(dp[i], (dp[i-j**2] + 1))

# print(dp[n])

############## 브루트포스(python으로도 통과)#################
# import math

# n = int(input())
# dp = [-1] * 50001
# # n이 제곱수일 때
# if int(math.sqrt(n)) == math.sqrt(n):
#     print(1)
#     exit()
# # n이 2개의 제곱수의 합일 때
# # 즉, sqrt(n - i**2)가 정수일 때
# for i in range(int(math.sqrt(n)), 0, -1):
#     if int(math.sqrt(n-i**2)) == math.sqrt(n-i**2):
#         print(2)
#         exit()
# # n이 3개의 제곱수의 합일 때
# # 즉 sqrt(n - i**2 - j**2)가 정수일 때
# for i in range(int(math.sqrt(n)), 0, -1):
#     for j in range(int(math.sqrt(n - i**2)), 0, -1):
#         if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
#             print(3)
#             exit()
# print(4)

#########################################
import math

n = int(input())

dp = [5] * 50001
for i in range(1, int(math.sqrt(n)) + 1):   # 제곱수들은 1로 초기화
    dp[i**2] = 1
    
def lag(n):
    if dp[n] == 1:
        return 1
    # n - i**2가 제곱수인 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        if dp[n-i**2] == 1:
            return 2
    # n - i**2 - j**2가 제곱수인 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n-i**2)) + 1):
            if dp[n-i**2-j**2] == 1:
                return 3
    return 4

print(lag(n))