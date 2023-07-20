n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
    
dx = [1, 0, 1]
dy = [0, 1, 1]

dp = [[0] * m for _ in range(n)]
dp[0][0] = maze[0][0]
for x in range(n):
    for y in range(m):
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y]+maze[nx][ny])
print(dp[n-1][m-1])