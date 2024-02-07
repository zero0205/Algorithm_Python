n, m, h = map(int, input().split())
map_data = []
sx, sy = 0, 0
mints = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            sx, sy = i, j
        elif row[j] == 2:
            mints.append((i, j))
    map_data.append(row)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [False] * len(mints)
ans = -1


def get_distance(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def bt(x, y, hp, drink):
    global ans
    if hp-get_distance(sx, sy, x, y) >= 0:
        ans = max(ans, drink)
    if drink >= len(mints):
        return
    for i in range(len(mints)):
        if not visited[i]:
            nx = mints[i][0]
            ny = mints[i][1]
            remain_hp = hp-get_distance(x, y, nx, ny)
            if remain_hp >= 0:
                visited[i] = True
                bt(nx, ny, remain_hp+h, drink+1)
                visited[i] = False


bt(sx, sy, m, 0)
print(ans)
