from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

dp = [[[int(1e9)]*2 for _ in range(m+1)] for _ in range(n+1)]
dp[hx][hy] = [0, 0]
q = deque([(hx, hy, False)])
while q:
    x, y, broke = q.popleft()
    if x == ex and y == ey:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 < nx <= n and 0 < ny <= m:
            if not broke:   # 벽 아직 안 뚫음
                if maze[nx-1][ny-1] == 0 and dp[nx][ny][0] > dp[x][y][0]+1:   # 이번에도 안 뚫음
                    dp[nx][ny][0] = dp[x][y][0]+1
                    q.append((nx, ny, broke))
                if maze[nx-1][ny-1] == 1 and dp[nx][ny][1] > dp[x][y][0]+1:  # 이번에 뚫음
                    dp[nx][ny][1] = dp[x][y][0]+1
                    q.append((nx, ny, True))
            elif broke and maze[nx-1][ny-1] == 0 and dp[nx][ny][1] > dp[x][y][1]+1:   # 이미 뚫은 적 있음
                dp[nx][ny][1] = dp[x][y][1]+1
                q.append((nx, ny, broke))

print(min(dp[ex][ey][0], dp[ex][ey][1]) if dp[ex][ey][0] != int(
    1e9) or dp[ex][ey][1] != int(1e9) else -1)
