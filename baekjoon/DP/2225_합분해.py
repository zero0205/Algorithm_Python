n, k = map(int, input().split())
dp = [[0] * (n+1) for _ in range(k+1)]  # 행은 사용한 정수 개수, 열은 만든 수

# 1개의 숫자로 N을 만드는 경우의 수는 1가지
for i in range(n+1):
    dp[1][i] = 1
# 0을 n개의 숫자로 만드는 경우도 1가지
for i in range(k+1):
    dp[i][0] = 1
    
if k > 1:
    for i in range(1, k+1):  # 사용한 정수 개수
        for j in range(1, n+1):  # 만든 수
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000
print(dp[k][n])