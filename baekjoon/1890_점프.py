n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0 or board[i][j] == 0:   # 올 방법이 없는 칸이거나 종착점
            continue
        # 오른쪽으로
        if j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]
        # 아래로
        if i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]
         
print(dp[-1][-1])