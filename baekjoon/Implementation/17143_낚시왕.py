from copy import deepcopy
import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    # 위치, 속력, 이동방향, 크기
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1] = [s, d-1, z]


def shark_move(x, y, s, d):
    # 상하
    if d < 2:
        cycle = (r-1) * 2
        # 위
        if d == 0:
            s += cycle - x
        # 아래
        else:
            s += x
        s %= cycle
        # 이동 후 방향이 위
        if s >= r:
            s = cycle - s
            d = 0
        # 이동 후 방향이 아래
        else:
            d = 1
        return s, y, d
    # 좌우
    else:
        cycle = (c-1) * 2
        # 오른
        if d == 2:
            s += y
        # 왼
        else:
            s += cycle - y
        s %= cycle
        # 이동 후 방향이 왼
        if s >= c:
            s = cycle - s
            d = 3
        # 이동 후 방향이 오른
        else:
            d = 2
        return x, s, d


ans = 0
for idx in range(c):
    # 상어 잡기
    for i in range(r):
        if board[i][idx] != []:
            ans += board[i][idx][2]
            board[i][idx] = []
            break
    # 상어 이동
    moved_shark = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != []:   # 상어가 있는 칸
                s, d, z = board[i][j]
                x, y, d = shark_move(i, j, s, d)
                if moved_shark[x][y] == [] or moved_shark[x][y][2] < z:
                    moved_shark[x][y] = [s, d, z]
    board = deepcopy(moved_shark)

print(ans)
#####################################
# r, c, m = map(int, input().split())
# board = [[[] for _ in range(c+1)] for _ in range(r+1)]
# for _ in range(m):
#     # 위치, 속력, 이동방향, 크기
#     x, y, s, d, z = map(int, input().split())
#     board[x][y] = [s, d, z]


# def shark_move(x, y, shark_info):
#     s, d, z = shark_info
#     dx = [0, -1, 1, 0, 0]
#     dy = [0, 0, 0, 1, -1]
#     # 상하
#     if d <= 2:
#         s %= (r-1)*2
#     # 좌우
#     else:
#         s %= (c-1)*2
#     for _ in range(s):
#         # 방향 전환
#         if d == 1 and x == 1:
#             d = 2
#         elif d == 2 and x == r:
#             d = 1
#         elif d == 3 and y == c:
#             d = 4
#         elif d == 4 and y == 1:
#             d = 3
#         x += dx[d]
#         y += dy[d]
#     return [x, y, s, d, z]


# ans = 0
# for idx in range(1, c+1):
#     # 상어 잡기
#     for i in range(1, r+1):
#         if board[i][idx] != []:
#             ans += board[i][idx][2]
#             board[i][idx] = []
#             break
#     # 상어 이동
#     moved_shark = []
#     for i in range(1, r+1):
#         for j in range(1, c+1):
#             if board[i][j] != []:   # 상어가 있는 칸
#                 moved_shark.append(shark_move(i, j, board[i][j]))
#                 board[i][j] = []
#     for x, y, s, d, z in moved_shark:
#         if board[x][y] == [] or board[x][y][2] < z:
#             board[x][y] = [s, d, z]

# print(ans)
