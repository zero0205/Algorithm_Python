r, c, t = map(int, input().split())
map_data = []
airclear = []   # 공기청정기 위치
for i in range(r):
    arr = list(map(int, input().split()))
    map_data.append(arr)
    for j in range(len(arr)):
        if arr[j] == -1:
            airclear.append([i, j]) # 공기청정기 위치 저장
# 우 상 좌 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 미세먼지 확산
def spread():   
    new_map = [[0] * c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if map_data[row][col] <= 0:
                continue
            cnt = 0
            for i in range(4):
                nx = row + dx[i]
                ny = col + dy[i]
                if 0 <= nx < r and 0 <= ny < c and map_data[nx][ny] != -1:
                    new_map[nx][ny] += map_data[row][col] // 5
                    cnt += 1
            map_data[row][col] -= (map_data[row][col] // 5) * cnt
    for row in range(r):
        for col in range(c):
            map_data[row][col] += new_map[row][col]
            
# 바람 순환
def wind(x, y, pos):    # 시작 위치(x, y), 공기청정기 위치(위(1)/아래(-1))
    # 1. 아래 / 위 이동
    while 0 < x < r-1:
        if map_data[x-pos][y] > 0:
            if map_data[x][y] != -1:    # 공기청정기가 아니라면
                map_data[x][y] = map_data[x-pos][y]
            map_data[x-pos][y] = 0
        x -= pos
    # 2. 왼쪽 이동
    while y < c-1:
        if map_data[x][y+1] > 0:  # 미세먼지 있는 칸
            map_data[x][y] = map_data[x][y+1]
            map_data[x][y+1] = 0
        y += 1
    # 3. 위 / 아래 이동
    if pos == 1:
        while x < airclear[0][0]:
            if map_data[x+1][y] > 0:
                map_data[x][y] = map_data[x+pos][y]
                map_data[x+1][y] = 0
            x += 1
    else:
        while x > airclear[1][0]:
            if map_data[x-1][y] > 0:
                map_data[x][y] = map_data[x-1][y]
                map_data[x-1][y] = 0
            x -= 1
    # 4. 오른쪽 이동
    while y > 0:
        if map_data[x][y-1] > 0:  # 미세먼지 있는 칸
            map_data[x][y] = map_data[x][y-1]
            map_data[x][y-1] = 0
        y -= 1

for i in range(t):
    # 미세먼지 확산
    spread()
    # 공기청정기 작동
    wind(airclear[0][0], airclear[0][1], 1)     # 윗 공기 순환
    wind(airclear[1][0], airclear[1][1], -1)    # 아랫 공기 순환

ans = 0
for i in range(r):
    for j in range(c):
        if map_data[i][j] > 0:
            ans += map_data[i][j]

print(ans)