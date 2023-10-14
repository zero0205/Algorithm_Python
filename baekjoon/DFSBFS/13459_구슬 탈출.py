from collections import deque

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(rx, ry, bx, by, 0)])
visited = []
visited.append((rx, ry, bx, by))
flag = False    # 성공 여부
while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt > 10:    # 10회 넘음
        break
    if board[rx][ry] == 'O':    # 빨간 구슬 구멍에 넣기 성공
        flag = True
        break
    for i in range(4):
        # 빨간 구슬
        nrx = rx + dx[i]
        nry = ry + dy[i]
        while True:
            if board[nrx][nry] == '#':  # 벽 부딪힘
                nrx -= dx[i]
                nry -= dy[i]
                break
            elif board[nrx][nry] == 'O':    # 구멍
                break
            nrx += dx[i]
            nry += dy[i]
        # 파란 구슬
        nbx = bx + dx[i]
        nby = by + dy[i]
        while True:
            if board[nbx][nby] == '#':  # 벽 부딪힘
                nbx -= dx[i]
                nby -= dy[i]
                break
            if board[nbx][nby] == 'O':  # 구멍
                break
            nbx += dx[i]
            nby += dy[i]

        if board[nbx][nby] == 'O':  # 파란 공이 구멍에 빠짐
            continue
        # 두 구슬이 맞부딪히는 경우 더 멀리서 온 구슬 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if (abs(nrx-rx)+abs(nry-ry)) > (abs(nbx-bx)+abs(nby-by)):
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        if (nrx, nry, nbx, nby) not in visited:
            q.append((nrx, nry, nbx, nby, cnt+1))
            visited.append((nrx, nry, nbx, nby))
print(1 if flag else 0)
