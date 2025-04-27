from collections import deque

n, m, fuel = map(int, input().split())
map_data = [[]]
for _ in range(n):
    map_data.append([1]+list(map(int, input().split())))
tx, ty = map(int, input().split())
customers = [[-1, -1, -1, -1]]
for i in range(1, m+1):
    sx, sy, ex, ey = map(int, input().split())
    map_data[sx][sy] = -i
    customers.append([sx, sy, ex, ey])


def get_nearest_customer(tx, ty):
    dists = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque([[tx, ty, 0]])
    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[tx][ty] = True
    while q:
        x, y, d = q.popleft()
        if map_data[x][y] < 0:
            sx, sy, ex, ey = customers[-map_data[x][y]]
            dists.append([d, sx, sy, ex, ey])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny] and map_data[nx][ny] <= 0:
                q.append([nx, ny, d+1])
                visited[nx][ny] = True
    if not dists:
        return None
    dists.sort()
    return dists[0]


def move_to_destination(sx, sy, ex, ey):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque([[sx, sy, 0]])
    visited = [[False]*(n+1) for _ in range(n+1)]
    visited[sx][sy] = True
    while q:
        x, y, d = q.popleft()
        # 승객을 태우고 목적지에 도착
        if x == ex and y == ey:
            return d
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 < nx <= n and 0 < ny <= n and not visited[nx][ny] and map_data[nx][ny] <= 0:
                q.append([nx, ny, d+1])
                visited[nx][ny] = True
    return int(1e9)


for _ in range(m):
    result = get_nearest_customer(tx, ty)
    if not result:
        fuel = -1
        break
    dist, sx, sy, ex, ey = result
    fuel -= dist
    if fuel < 0:
        fuel = -1
        break
    dist = move_to_destination(sx, sy, ex, ey)
    fuel -= dist
    if fuel < 0:
        fuel = -1
        break
    fuel += dist*2
    map_data[sx][sy] = 0
    tx, ty = ex, ey

print(fuel)
