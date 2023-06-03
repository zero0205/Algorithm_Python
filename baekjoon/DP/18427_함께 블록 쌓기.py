# from collections import defaultdict

# n, m, h = map(int, input().split())
# dp = defaultdict(int)
# dp[0] += 1
# for _ in range(n):
#     possible = []
#     for num in list(map(int, input().split())):
#         for i in dp.keys():
#             possible.append((i+num, dp[i]))
#     for a, b in possible:
#         dp[a] += b
# print(dp[h]%10007)

####################################
n, m, h = map(int, input().split())
dp = [[0]*(h+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    # i번째 학생의 블럭을 사용하지 않는 경우
    for j in range(h+1):
        dp[i][j] = dp[i-1][j]
    # i번째 학생의 블럭을 사용하는 경우
    for block in list(map(int, input().split())):
        for j in range(block, h+1):
            dp[i][j] += dp[i-1][j-block]
print(dp[-1][h]%10007)