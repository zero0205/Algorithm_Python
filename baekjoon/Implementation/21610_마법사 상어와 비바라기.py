import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# 격자 정보 입력
map_data = []   # 격자
for _ in range(n):
    map_data.append(list(map(int, input().split())))
    
move_dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = deque([[n-1, 0],[n-1, 1],[n-2, 0],[n-2, 1]])    # 구름 위치

def cloud_move(d, s, disappear):
    rain = deque()
    while cloud:
        x, y = cloud.popleft()
        nx = (x + move_dir[d-1][0] * s) % n
        ny = (y + move_dir[d-1][1] * s) % n
        map_data[nx][ny] += 1
        disappear[nx][ny] = True    # 구름이 사라진 위치 표시
        rain.append([nx, ny])
    return rain # 비가 내려서 물이 증가한 칸들

def water_bug(r, c):
    for i in range(4):
        nr = r + move_dir[2*i+1][0]
        nc = c + move_dir[2*i+1][1]
        if 0 <= nr < n and 0 <= nc < n:
            if map_data[nr][nc] > 0:
                map_data[r][c] += 1
            
def cloud_create(disappear):
    for i in range(n):
        for j in range(n):
            if map_data[i][j] >= 2 and not disappear[i][j]:
                cloud.append([i, j])
                map_data[i][j] -= 2
        
# 이동 정보
for _ in range(m):
    d, s = map(int, input().split())
    disappear = [[False] * n for _ in range(n)]
    rain = cloud_move(d, s, disappear)
    while rain:
        r, c = rain.popleft()
        water_bug(r, c) # 비가 내려서 물이 증가한 칸들에 물복사버그 마법 시전
    cloud_create(disappear)
        
ans = 0
for i in range(n):
    for j in range(n):
        ans += map_data[i][j]
print(ans)