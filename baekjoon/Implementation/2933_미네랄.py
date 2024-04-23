from collections import deque
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))
dir = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def drop(sx, sy):
    # BFS => 클러스터 찾기
    q = deque([(sx, sy)])
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True
    cluster = [[sx, sy]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == 'x':
                q.append((nx, ny))
                visited[nx][ny] = True
                cluster.append([nx, ny])
    # 클러스터 각 열의 최소 높이 찾기
    lowest = dict()
    for cx, cy in cluster:
        if cy not in lowest or lowest[cy] < cx:
            lowest[cy] = cx
    # 얼마나 떨어져야할지 구하기
    drop_height = 101   # 클러스터가 떨어져야할 최소 높이
    for j in lowest.keys():  # 열
        if lowest[j] == r-1:  # 바닥에 닿는 클러스터임 => 안 떨어져도 됨
            return False
        for i in range(lowest[j]+1, r):
            if board[i][j] == 'x':
                drop_height = min(drop_height, i-lowest[j]-1)
                break
            if i+1 == r:
                drop_height = min(drop_height, i-lowest[j])
    # 떨어져라
    cluster.sort(key=lambda x: -x[0])
    for cx, cy in cluster:
        board[cx][cy] = '.'
        board[cx+drop_height][cy] = 'x'
    return True  # 클러스터 떨어짐


def throw(h, dir):
    if dir == 1:
        for j in range(c):
            if board[h][j] == 'x':  # 미네랄과 충돌
                board[h][j] = '.'
                return [h, j]
    else:
        for j in range(c-1, -1, -1):
            if board[h][j] == 'x':  # 미네랄과 충돌
                board[h][j] = '.'
                return [h, j]
    return [-1, -1]


for h in heights:
    h = r-h
    x, y = throw(h, dir)
    if x == -1 and y == -1:  # 미네랄과 안 부딪힘
        dir *= -1
        continue
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'x':
            if drop(nx, ny):
                break   # 한 번에 한 개의 클러스터만 떨어짐
    dir *= -1
# 출력
for i in range(r):
    print(*board[i], sep='')
