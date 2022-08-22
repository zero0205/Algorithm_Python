# str1 = input()
# str2 = input()

# dp = [["" for _ in (range(len(str1) + 1))] for _ in range(len(str2) + 1)]

# for i in range(1, len(str2) + 1):
#     for j in range(1, len(str1) + 1):
#         if str1[j-1] == str2[i-1]:
#             dp[i][j] = dp[i-1][j-1] + str1[j-1]
#         else:
#             if len(dp[i-1][j]) < len(dp[i][j-1]):
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i-1][j]

# print(len(dp[len(str2)][len(str1)]))
# print(dp[len(str2)][len(str1)])

#####################################
str1 = input()
str2 = input()

dp = [[0 for _ in (range(len(str1) + 1))] for _ in range(len(str2) + 1)]
ans = ""
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

row, col = len(str2), len(str1)           
while len(ans) < dp[len(str2)][len(str1)]:
    if str1[col-1] == str2[row-1] and dp[row-1][col-1] + 1 == dp[row][col]:
        ans = str1[col-1] + ans
        row -= 1
        col -= 1 
    elif dp[row][col] == dp[row-1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col-1]:
        col -= 1
print(dp[len(str2)][len(str1)])
print(ans)