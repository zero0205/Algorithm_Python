m, n = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(m)]

dp = [[0]*(n+1) for _ in range(m+1)]
answer = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if map_data[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            if dp[i][j] > answer:
                answer = dp[i][j]
print(answer)
