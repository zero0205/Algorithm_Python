m, n = map(int, input().split())
map_data = []
for _ in range(m):
    map_data.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dp = [[-1] * n for _ in range(m)]

def dfs(x, y):
    if x == m-1 and y == n-1:   # 목적지 도달
        return 1
    
    if dp[x][y] != -1:  # 이미 방문한 칸
        return dp[x][y] # x, y까지 가능한 경로의 수 리턴
    
    dp[x][y] = 0    # 방문 표시
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if map_data[nx][ny] < map_data[x][y]:   # 높이가 더 낮은 지점으로
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))