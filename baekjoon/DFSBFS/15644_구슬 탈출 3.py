from collections import deque

n, m = map(int, input().split())
board = []
rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        if row[j] == 'R':
            rx, ry = i, j
        elif row[j] == 'B':
            bx, by = i, j
    board.append(row)

# BFS
q = deque([(rx, ry, bx, by, '')])
visited = set()
visited.add((rx, ry, bx, by))
board[rx][ry] = '.'
board[bx][by] = '.'
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dd = ['L', 'R', 'U', 'D']


def marble_move(x, y, d):   # 구슬 이동
    while True:
        x += dx[d]
        y += dy[d]
        if board[x][y] == 'O':
            return [x, y]
        if board[x][y] == '#':
            x -= dx[d]
            y -= dy[d]
            return [x, y]


while q:
    rx, ry, bx, by, mv = q.popleft()
    if len(mv) >= 10:
        break
    for i in range(4):
        nrx, nry = marble_move(rx, ry, i)   # 빨간 구슬 이동
        nbx, nby = marble_move(bx, by, i)   # 파란 구슬 이동
        if board[nbx][nby] == 'O':  # 파란 구슬이 구멍에 빠지는 경우
            continue
        if board[nrx][nry] == 'O':  # 빨간 구슬이 구멍에 빠지는 경우
            print(len(mv)+1)
            print(mv+dd[i])
            exit()
        if nrx == nbx and nry == nby:   # 빨간 구슬과 파란 구슬이 겹치는 상황
            if abs(nrx-rx)+abs(nry-ry) < abs(nbx-bx)+abs(nby-by):
                nbx -= dx[i]
                nby -= dy[i]
            else:
                nrx -= dx[i]
                nry -= dy[i]
        if (nrx, nry, nbx, nby) not in visited:
            q.append((nrx, nry, nbx, nby, mv+dd[i]))
            visited.add((nrx, nry, nbx, nby))

print(-1)
