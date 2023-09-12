from copy import deepcopy

dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0),
       (1, 1), (0, 1), (-1, 1)]   # 위부터 반시계방향

ans = 0
board = [[[] for _ in range(4)] for _ in range(4)]


def fish_move(board, shark_x, shark_y):
    for fish in range(1, 17):
        find_fish = False
        for i in range(4):
            if find_fish:
                break
            for j in range(4):
                if board[i][j][0] == fish:
                    x, y = i, j
                    find_fish = True
                    break
        if not find_fish:   # 이미 잡아먹힌 물고기
            continue
        for i in range(8):
            nd = (board[x][y][1]+i) % 8
            nx = x + dir[nd][0]
            ny = y + dir[nd][1]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == shark_x and ny == shark_y):
                continue
            # 자리 바꾸기
            board[x][y] = board[nx][ny]
            board[nx][ny] = [fish, nd]
            break


def dfs(board, x, y, eat):
    global ans
    eat += board[x][y][0]
    board[x][y][0] = 0
    # 물고기 이동
    fish_move(board, x, y)
    # 상어 이동
    for i in range(1, 5):
        nx = x + dir[board[x][y][1] % 8][0] * i
        ny = y + dir[board[x][y][1] % 8][1] * i
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or board[nx][ny][0] == 0:
            continue
        dfs(deepcopy(board), nx, ny, eat)
    ans = max(ans, eat)
    return


# 입력
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        n, d = row[j], row[j+1]
        board[i][j//2] = [n, d-1]

dfs(board, 0, 0, 0)
print(ans)
