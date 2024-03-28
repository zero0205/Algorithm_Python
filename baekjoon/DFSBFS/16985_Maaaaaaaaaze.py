from collections import deque
from itertools import permutations

boards = [[list(map(int, input().split())) for _ in range(5)]
          for _ in range(5)]
ans = 126


def rotate(board):  # 판을 시계 방향 회전
    new_board = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_board[j][4-i] = board[i][j]
    return new_board


def bfs(cube):  # 경로 탐색
    global ans
    q = deque([(0, 0, 0, 0)])
    dist = [[[False]*5 for _ in range(5)] for _ in range(5)]
    dist[0][0][0] = True

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        x, y, z, cnt = q.popleft()
        if cnt > ans:
            return
        if x == 4 and y == 4 and z == 4:
            ans = min(ans, cnt)
            if cnt == 12:
                print(cnt)
                exit()
            return
        for d in range(6):
            nx = x+dx[d]
            ny = y+dy[d]
            nz = z+dz[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and not dist[nx][ny][nz] and cube[nx][ny][nz] == 1:
                q.append((nx, ny, nz, cnt+1))
                dist[nx][ny][nz] = True
    return


def dfs(cube, idx):  # 각 판의 회전
    if idx == 5:
        if cube[0][0][0] and cube[4][4][4]:
            bfs(cube)
        return
    for _ in range(4):
        dfs(cube, idx+1)
        cube[idx] = rotate(cube[idx])


for comb in permutations(range(5)):  # 판 순서
    cube = []
    for i in comb:
        cube.append(boards[i])
    dfs(cube, 0)
print(ans if ans <= 125 else -1)
