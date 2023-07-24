# n = int(input())
# score = list(map(int, input().split()))

# dp = [0] * (n+1)
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         dp[i] = max(dp[i], dp[i-j]+(max(score[i-j:i])-min(score[i-j:i])))

# print(dp[n])
###########################################################
n = int(input())
score = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i]
    max_v = min_v = score[i]
    j = i-1
    while j >= 0 and (score[j] < min_v or score[j] > max_v):
        max_v = max(score[j], max_v)
        min_v = min(score[j], min_v)
        dp[i+1] = max(dp[i+1], dp[j]+(max_v-min_v))
        j -= 1

print(dp[n])