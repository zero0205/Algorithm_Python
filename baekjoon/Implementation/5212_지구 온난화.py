r, c = map(int, input().split())
map_data = []
for _ in range(r):
    map_data.append(list(input()))

# 섬이 사라질지 말지?
def island_remove(x, y):
    cnt = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        # 바다인지
        if (nx < 0 or nx >= r or ny < 0 or ny >= c) or map_data[nx][ny] == '.':
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

# 사라진 섬들 처리  
def map_change(arr):
    for x, y in arr:
        map_data[x][y] = '.'

# 맵 데이터 출력
def print_map():
    sr, er = 0, r-1 # 시작행, 끝나는행
    sc, ec = 0, c-1 # 시작열, 끝나는열
    sr_find, er_find = False, False
    sc_find, ec_find = False, False
    # 지도 시작하는 행, 끝나는 행 찾기
    for i in range(r//2+1):
        if sr_find and er_find:
            break
        for j in range(c):
            # 시작행
            if map_data[i][j] == 'X' and not sr_find:
                sr = i
                sr_find = True
            # 끝나는 행
            if map_data[r-1-i][j] == 'X' and not er_find:
                er = r-1-i
                er_find = True
    # 지도 시작하는 열, 끝나는 열 찾기
    for i in range(c//2+1):
        if sc_find and ec_find:
            break
        for j in range(r):
            # 시작열
            if map_data[j][i] == 'X' and not sc_find:
                sc = i
                sc_find = True
            # 끝나는 열
            if map_data[j][c-1-i] == 'X' and not ec_find:
                ec = c-1-i
                ec_find = True
    # 맵 출력
    for i in range(sr, er+1):
        for j in range(sc, ec+1):
            print(map_data[i][j], end='')
        print()
 
remove_islands = []
for i in range(r):
    for j in range(c):
        if map_data[i][j] == 'X':
            if island_remove(i, j):
                remove_islands.append((i, j))
map_change(remove_islands)            
print_map()