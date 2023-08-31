from itertools import combinations
from collections import deque

n, m = map(int, input().split())
blank = []
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            blank.append((i, j))


def bfs(x, y, visited):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(x, y)])

    visited[x][y] = True
    res = 1
    flag = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    flag = False
                    continue
                elif board[nx][ny] == 1:
                    continue
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    res += 1
    return res if flag else 0


ans = -1
for a, b in combinations(blank, 2):
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    # 돌 놓기
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    # 죽일 수 있는 상대방 돌 개수 계산
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and not visited[i][j]:
                cnt += bfs(i, j, visited)
    # 돌 회수
    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    ans = max(ans, cnt)
print(ans)
