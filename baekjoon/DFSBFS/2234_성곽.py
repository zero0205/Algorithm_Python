from collections import deque

n, m = map(int, input().split())
castle = []
for _ in range(m):
    castle.append(list(map(int, input().split())))
# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y, num):
    q = deque([(x, y)])
    room_num[x][y] = num
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if castle[x][y] & (1 << i) == 0 and room_num[nx][ny] == -1:
                q.append((nx, ny))
                room_num[nx][ny] = num
                cnt += 1
    return cnt


def find_neighbor(x, y):
    q = deque([(x, y)])
    visited = [[False]*n for _ in range(m)]
    visited[x][y] = True
    neighbor = set()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                if room_num[x][y] == room_num[nx][ny]:  # 같은 방
                    q.append((nx, ny))
                else:   # 이웃 방
                    neighbor.add(room_num[nx][ny])
                visited[nx][ny] = True
    return neighbor


room = []
room_start = []
room_num = [[-1]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if room_num[i][j] == -1:
            room.append(bfs(i, j, len(room)))
            room_start.append([i, j])
print(len(room))
print(max(room))
remove_one = -1
for i in range(len(room)):
    r, c = room_start[i]
    for neighbor in list(find_neighbor(r, c)):
        remove_one = max(remove_one, room[neighbor]+room[i])
print(remove_one)
