# n = int(input())
# arr = list(map(int, input().split()))

# if n == 1:
#     print(0)
#     exit()
# if n == 2:
#     print(0 if arr[0] == arr[1] else 1)
#     exit()
    
# ans = 5000
# # 하나씩 거꾸로 가며 확인
# for i in range(n):
#     prefix, suffix = i, i+2
#     num = 0
#     while suffix < n:
#         if arr[suffix] == arr[prefix]:
#             suffix += 1
#             num += 1
#         prefix -= 1
#         if suffix == n:
#             ans = min(ans, i+1-num)
#         if prefix < 0:
#             break
# print(ans)

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]  # arr i번째까지의 수열과 arr의 역순수열의 j번째까지의 수열의 최장공통수열 길이 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i-1] == arr[n-j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(n-dp[n][n])