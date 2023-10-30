from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
island = [[0]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = int(1e6)


def island_numbering(x, y, num):
    q = deque([(x, y)])
    island[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if island[nx][ny] == 0 and board[nx][ny] == 1:
                    q.append((nx, ny))
                    island[nx][ny] = num


def connect_island(num):
    visited = [[False]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if island[i][j] == num:
                q.append((i, j, 0))
                visited[i][j] = True

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if island[nx][ny] != num and island[nx][ny] > 0:
                    return dist
                elif island[nx][ny] == 0:
                    q.append((nx, ny, dist+1))
                    visited[nx][ny] = True


# 섬 번호 부여
num = 1
for i in range(n):
    for j in range(n):
        if island[i][j] == 0 and board[i][j] == 1:
            island_numbering(i, j, num)
            num += 1

# 다리 연결
for i in range(1, num):
    ans = min(ans, connect_island(i))
print(ans)
