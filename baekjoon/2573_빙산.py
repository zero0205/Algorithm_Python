from collections import deque

n, m = map(int, input().split())
map_data = []
ice = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if map_data[i][j] != 0:
            ice.append((i, j))

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True    # 방문 처리
    sea = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if map_data[nx][ny] == 0:    # 지금 탐색한 옆칸이 바다라면
                cnt += 1
            elif map_data[nx][ny] > 0 and not visited[nx][ny]:  # 아직 탐색 안한 붙어있는 빙산
                q.append((nx, ny))
                visited[nx][ny] = True
        if cnt > 0: # 바다와 닿은 부분이 있음
            sea.append((x, y, cnt)) 
    for x, y, cnt in sea:
        map_data[x][y] -= cnt   # 바다와 닿은 면적만큼 녹음
        if map_data[x][y] < 0:
            map_data[x][y] = 0

year = 0

while ice:
    tmp = 0  
    visited = [[False for _ in range(m)] for _ in range(n)]
    delList = []
    
    for x, y in ice:
        if not visited[x][y]:   # 아직 방문하지 않은 빙산이라면 BFS
            bfs(x, y)
            tmp += 1
        if map_data[x][y] == 0:
            delList.append((x, y))  # 다 녹은 빙산 delList에 추가
            
    if tmp > 1: # 빙산이 2 덩어리 이상으로 쪼개짐
        print(year)
        exit()
    ice = sorted(list(set(ice) - set(delList)))
    year += 1
    
print(0)