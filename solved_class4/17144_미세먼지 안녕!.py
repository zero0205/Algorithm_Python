import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
map_data = []
for _ in range(r):
    map_data.append(list(map(int, input().split())))
    
for i in range(r):
    if map_data[i][0] == -1:    # 공기청정기 위치(항상 1열에 위치, 크기는 2)
        up = i
        down = i + 1
        break
                 
# 미세먼지 확산
def dust_spread(sec):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    tmp_map = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            num = 0
            if map_data[x][y] > 0:           
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and map_data[nx][ny] != -1:
                        tmp_map[nx][ny] += map_data[x][y] // 5
                        num += 1
                map_data[x][y] -= num * (map_data[x][y] // 5)
    for x in range(r):
        for y in range(c):
            map_data[x][y] += tmp_map[x][y]
            
# 윗공기 순환
def up_air():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    dir = 0
    prev = 0
    x, y = up, 1
    
    while True:
        nx = x + dx[dir % 4]
        ny = y + dy[dir % 4]
        # 공기청정기로 되돌아가면 끝
        if x == up and y == 0:
            break
        # 범위를 벗어나면 방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue     
        
        # 미세먼지 한 칸 밀려남
        map_data[x][y], prev = prev, map_data[x][y]

        x, y = nx, ny

    
# 아랫공기 순환
def down_air():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    dir = 0
    prev = 0
    x, y = down, 1
    
    while True:
        nx = x + dx[dir % 4]
        ny = y + dy[dir % 4]
        # 공기청정기로 되돌아가면 끝
        if x == down and y == 0:
            break
        # 범위를 벗어나면 방향 전환
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        # 미세먼지 한 칸 밀려남
        map_data[x][y], prev = prev, map_data[x][y]
            
        x, y = nx, ny
            
for sec in range(t):
    # 미세먼지 확산
    dust_spread(sec)
    
    # 공기청정기 작동
    up_air()
    down_air()
    
# 남아있는 미세먼지의 양 계산
answer = 0
for i in range(r):
    for j in range(c):
        if map_data[i][j] > 0:
            answer += map_data[i][j]
            
print(answer)