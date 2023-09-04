from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
h, w, sr, sc, fr, fc = map(int, input().split())

# 누적합 계산
acc = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        acc[i][j] = acc[i-1][j]+acc[i][j-1]-acc[i-1][j-1]+board[i-1][j-1]

# 직사각형 범위 안에 벽이 있는지 확인


def wall_exist(r, c):
    if acc[r+h-1][c+w-1] - acc[r+h-1][c] - acc[r][c+w-1] + acc[r-1][c-1] > 0:
        return True
    else:
        return False


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
q = deque([(sr-1, sc-1, 0)])
visited = [[False]*m for _ in range(n)]
visited[sr-1][sc-1] = True
while q:
    r, c, cnt = q.popleft()
    if r == fr-1 and c == fc-1:
        print(cnt)
        exit()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr+h-1 < n and nc >= 0 and nc+w-1 < m and not visited[nr][nc]:
            if acc[nr+h][nc+w]-acc[nr+h][nc]-acc[nr][nc+w]+acc[nr][nc] == 0:
                q.append((nr, nc, cnt+1))
                visited[nr][nc] = True
print(-1)
