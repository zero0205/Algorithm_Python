from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)

for _ in range(int(input())):
    w, h = map(int, input().split())
    board = []  # 빌딩 지도
    x, y = -1, -1   # 상근이 위치
    fire = []   # 불의 위치
    fire_board = [[INF]*w for _ in range(h)]    # 각 칸에 불 붙는데 걸리는 시간
    for i in range(h):
        row = list(input())
        for j in range(w):
            if row[j] == '@':   # 상근이의 초기 위치
                x = i
                y = j
            elif row[j] == '*':  # 초기 불들의 위치
                fire.append((i, j))
                fire_board[i][j] = 0
        board.append(row)
    # 칸마다 불이 붙는 시간 구하기
    q = deque(fire)
    while q:
        fx, fy = q.popleft()
        for d in range(4):
            nx = fx + dx[d]
            ny = fy + dy[d]
            if 0 <= nx < h and 0 <= ny < w and fire_board[nx][ny] > fire_board[fx][fy]+1 and board[nx][ny] == '.':
                q.append((nx, ny))
                fire_board[nx][ny] = fire_board[fx][fy]+1
    # 탈출 가능한지
    q = deque([(x, y, 0)])
    board[x][y] = '_'
    ans = -1
    while q:
        x, y, s = q.popleft()
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            ans = s+1
            break
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and fire_board[nx][ny] > s+1:
                q.append((nx, ny, s+1))
                board[nx][ny] = '_'
    print(ans if ans > 0 else "IMPOSSIBLE")
