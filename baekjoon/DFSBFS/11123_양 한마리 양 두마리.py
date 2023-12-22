from collections import deque


def bfs(sx, sy, board):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(sx, sy)])
    board[sx][sy] = '-'
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '#':
                q.append((nx, ny))
                board[nx][ny] = '-'


for _ in range(int(input())):
    h, w = map(int, input().split())
    board = [[] for _ in range(h)]
    for i in range(h):
        board[i] = list(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '#':
                ans += 1
                bfs(i, j, board)
    print(ans)
