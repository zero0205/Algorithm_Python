# https://www.acmicpc.net/problem/16236

from collections import deque

INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2
eating_fish_num = 0
fish_location = []
sec = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for r in range(n):
    for c in range(n):
        if arr[r][c] == 9:  # 상어 위치
            shark_location = (r, c)

# 먹을 수 있는 물고기 리스트 리턴
def possible_fish(shark_size, arr):
    lst = []
    for r in range(n):
        for c in range(n):
            # 빈 칸 아니고 상어 사이즈보다 작으면
            if arr[r][c] != 0 and arr[r][c] < shark_size:
                lst.append((r,c))
    return lst

# 상어가 물고기 먹으러 가는 거리 계산
def shark_eat(sr, sc, fr, fc):
    q = deque([(sr, sc)])
    dist = [[INF] * n for _ in range(n)]
    dist[sr][sc] = 0
    while q:
        r, c= q.popleft()
        # 물고기 위치에 도달
        if r == fr and c == fc:
            return dist[r][c]
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            # 범위 내에 있고 아직 방문하지 않은 칸이라면 진행
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == INF:
                if arr[nr][nc] > shark_size:    # 나보다 큰 물고기 있는 칸은 못 지나감
                    continue
                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1
     
while True:
    # 현재 먹을 수 있는 물고기 리스트 업데이트
    possible_fish_lst = possible_fish(shark_size, arr)
    # 먹을 수 있는 물고기가 없다면 break
    if not possible_fish_lst:
        print(sec)
        break
    # 먹을 수 있는 물고기 중 최단 거리를 갖는 물고기 찾음
    min_dist = INF
    for fish in possible_fish_lst:
        dist = shark_eat(shark_location[0], shark_location[1], fish[0], fish[1])
        # 거리가 가장 가까운 물고기 중 가장 먼저 저장되는 값이 가장 위쪽, 왼쪽일것
        if dist < min_dist: 
            eat_r, eat_c = fish
            min_dist = dist
    # 물고기 먹고 상태 업데이트
    sec += min_dist
    # 상어 상태(위치, 크기) 업데이트
    arr[shark_location[0]][shark_location[1]] = 0
    shark_location = eat_r, eat_c
    eating_fish_num += 1
    if eating_fish_num == shark_size:   # 본인 크기만큼의 물고기 먹으면 사이즈업
        shark_size += 1
        eating_fish_num = 0
    # 먹은 물고기 있던 위치 상어로 표시
    arr[eat_r][eat_c] = 9