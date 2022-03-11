# https://www.acmicpc.net/problem/19237

# n : 격자 가로세로 크기, m : 처음 상어 마릿수, k : 냄새 남는 시간
n, m, k = map(int, input().split())
# 격자 입력받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
# 각 상어의 방향 (1 ~ m번 상어까지) (1:위, 2:아래, 3: 왼쪽, 4: 오른쪽)
shark_dir = list(map(int, input().split()))
# 각 상어의 방향 우선순위 입력받기
dir_order = [[] for _ in range(m + 1)]
for i in  range(1, m + 1):
    for _ in range(4):  # 각 상어별 우선순위 (위, 아래, 왼, 오 순서)
        dir_order[i].append(list(map(int, input().split())))
        

# 위 아래 왼 오(1,2,3,4)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어가 다음에 이동할 칸 위치 반환
def shark_move(array, x, y):
    my_scent = None
    shark_num = array[x][y]
    for i in range(4):
        next_dir = dir_order[shark_num][shark_dir[shark_num - 1] - 1][i]
        nx = x + dx[next_dir - 1]
        ny = y + dy[next_dir - 1]
        # 범위를 벗어남
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 이미 냄새가 있음
        elif shark_scent[nx][ny][0] != 0:
            # 내 냄새이고 가장 먼저 나온 것
            if shark_scent[x][y][0] == shark_scent[nx][ny][0] and my_scent == None:
                my_scent = (nx, ny)
            continue
        # 아무 냄새가 없음
        else:
            return (nx, ny)
    # 인접한 칸 중 아무 냄새가 없는 칸이 없다면 내 냄새 있는 칸으로
    return my_scent

# 상어 냄새 지도
shark_scent = [[(0, 0)] * n for _ in range(n)]
# 상어 번호별 현재 위치
shark_location = [[None] for _ in range(m + 1)]

# 처음 상어들 위치 파악
for row in range(n):
    for col in range(n):
        if array[row][col] == 0:
            continue
        else:
            shark_location[array[row][col]] = (row, col)
            shark_scent[row][col] = (array[row][col], k)    # 상어 번호와 남은 지속 시간
          
result = 0

while m > 1:
    for shark in shark_location[1:]:
        if shark == None:   # 쫓겨난 상어
            continue   
        now_x, now_y = shark 
        next_location = shark_move(array, shark[0], shark[1])
        # 나보다 번호 작은 상어 있으면 쫓겨남
        if array[next_location[0]][next_location[1]] != 0:
            shark = None
            m -= 1
            continue
        else:
            # array 업데이트
            array[next_location[0]][next_location[1]] = array[now_x][now_y]
            array[now_x][now_y] = 0
            # 상어 현재 위치 갱신
            shark = next_location
            # 이동한 칸에 향기 뿌리기
            shark_scent[next_location[0]][next_location[1]] = (array[next_location[0]][next_location[1]], k + 1)    # 나중에 전체 지속시간에 대해 1 뺴줄거라서 k+1
    
    # 향기 지속 시간 1씩 감소
    for row in shark_scent:
        for col in row:
            if col == (0, 0):
                continue
            col = (col[0], col[1] - 1)
            # 지속 시간이 0됨
            if col[1] == 0:
                col = (0, 0)
    result += 1
    
print(result)