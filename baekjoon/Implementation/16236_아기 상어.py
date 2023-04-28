from heapq import heappush, heappop
from collections import deque

shark_size = 2  # 아기 상어 크기
sx, sy = 0, 0   # 아기 상어 위치
shark_eat = 0   # 아기 상어가 먹은 물고기 수

n = int(input())
map_data = []
fishes = []

def get_dist(x, y):
    global sx, sy, shark_size
    
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    
    q = deque([[sx, sy, 0]])    # 아기 상어 위치
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    while q:
        now_x, now_y, cnt = q.popleft() 
        if now_x == x and now_y == y:
            return cnt
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] <= shark_size and not visited[nx][ny]:
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = True
    return 401  # 도달할 수 없는 경우

def get_fish_list():
    fishes = []
    for i in range(n):
        for j in range(n):
            if 0 < map_data[i][j] < shark_size:    # 먹을 수 있는 물고기 위치
                heappush(fishes, (get_dist(i, j), i, j))
    return fishes
    
for i in range(n):
    map_data.append(list(map(int, input().split())))
    for j in range(n):
        if map_data[i][j] == 9: # 아기 상어
            sx, sy = i, j
            map_data[i][j] = 0
            
fishes = get_fish_list()
ans = 0
while fishes:
    dist, x, y = heappop(fishes)
    if dist == 401:
        break
    ans += dist
    shark_eat += 1
    map_data[sx][sy] = 0    # 원래 상어 있던 자리 빈 칸으로
    sx, sy = x, y
    map_data[sx][sy] = 0    # 상어 위치 0으로 업데이트
    
    if shark_eat >= shark_size: # 상어 사이즈 업
        shark_size += 1
        shark_eat = 0
    fishes = get_fish_list()    # 상어에서 다른 물고기들까지 거리 업데이트
print(ans)