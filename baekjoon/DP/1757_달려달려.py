n, m = map(int, input().split())
d = [0]+[int(input()) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]  # i분에 지침 지수가 j일 때 최대 이동 거리
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i][0])    # 지침 지수 0에서 계속 쉬는 경우
    for j in range(1, m+1):
        if j == 1 or dp[i-1][j-1] != 0:  # 달리기
            dp[i][j] = dp[i-1][j-1]+d[i]
            if (i+j <= n):  # i분이고 지침 지수 j인 상황에서 쭉 쉬는 경우
                dp[i+j][0] = max(dp[i][j], dp[i+j][0])

print(dp[n][0])
