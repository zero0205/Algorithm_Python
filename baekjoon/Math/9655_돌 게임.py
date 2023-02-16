# n = int(input())
# if n % 2 == 0:
#     print("CY")
# else:
#     print("SK")

######## DP #########
n = int(input())
dp = [0, 1, 2, 1]   # n개의 돌이 있을 때 두 사람이 최소로 게임을 진행하는 횟수
if n >= 3:
    for i in range(3, n + 1):
        dp.append(min(dp[i-1], dp[i-3]))

if dp[n] % 2 == 1:
    print("SK")
else:
    print("CY")