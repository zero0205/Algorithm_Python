n, m, x, y, k = map(int, input().split())
# 위->아래: 북->남 / 왼->오: 서->동
map_data = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dice = [0]*6
top = 0  # 윗면
up = 1  # 북쪽
right = 2   # 동쪽

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for o in orders:    # 명령
    nx = x+dx[o-1]
    ny = y+dy[o-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    if o == 1:  # 동
        if map_data[x][y] == 0:
            map_data[x][y] = dice[right]
        else:
            dice[right] = map_data[x][y]
            map_data[x][y] = 0
        top, right = 5-right, top
    elif o == 2:  # 서
        if map_data[x][y] == 0:
            map_data[x][y] = dice[5-right]
        else:
            dice[5-right] = map_data[x][y]
            map_data[x][y] = 0
        top, right = right, 5-top
    elif o == 3:  # 북
        if map_data[x][y] == 0:
            map_data[x][y] = dice[up]
        else:
            dice[up] = map_data[x][y]
            map_data[x][y] = 0
        top, up = 5-up, top
    else:   # 남
        if map_data[x][y] == 0:
            map_data[x][y] = dice[5-up]
        else:
            dice[5-up] = map_data[x][y]
            map_data[x][y] = 0
        top, up = up, 5-top
    print(dice[top])
