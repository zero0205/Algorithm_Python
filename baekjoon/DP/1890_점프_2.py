n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if i+board[i][j] < n:
            dp[i+board[i][j]][j] += dp[i][j]
        if j+board[i][j] < n:
            dp[i][j+board[i][j]] += dp[i][j]
print(dp[n-1][n-1])