n = int(input())

dp = [0, 0, 1, 1] 
for i in range(4, n+1):
    if i % 3 == 0 and i % 2 == 0:  # 6의 배수
        dp.append(min(dp[i//3], dp[i//2], dp[i-1]) + 1)
    elif i % 3 == 0:    # 3의 배수
        dp.append(min(dp[i//3], dp[i-1]) + 1)
    elif i % 2 == 0:    # 2의 배수
        dp.append(min(dp[i//2], dp[i-1]) + 1)
    else:
        dp.append(dp[i-1] + 1)
    
print(dp[n])

###############################################
# n = int(input())

# dp = [1000001] * 1000001
# dp[0], dp[1] = 0, 0
# for i in range(2, n+1):
#     if i % 3 == 0:  
#         dp[i] = min(dp[i//3] + 1, dp[i])
#     if i % 2 == 0:
#         dp[i] = min(dp[i//2] + 1, dp[i])
#     dp[i] = min(dp[i-1] + 1, dp[i])
    
# print(dp[n])