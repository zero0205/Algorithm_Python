from collections import deque

n, k, r = map(int, input().split())
# 길 정보
road = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1][c1].append([r2, c2])
    road[r2][c2].append([r1, c1])
    
# 소의 위치
cow_position = []
for _ in range(k):
    cow_position.append(list(map(int, input().split())))

# BFS
def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 소가 길을 건너지 않고 갈 수 있는 모든 곳을 탐색
    while q:
        row, col = q.popleft()
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            # 범위를 벗어나면 안됨
            if nr < 1 or nr > n or nc < 1 or nc > n:
                continue
            # 이미 방문한 곳일 때
            if visited[nr][nc]:
                continue
            # 길을 건너야하는 경우
            if [nr, nc] in road[row][col]:
                continue
            q.append((nr, nc))
            visited[nr][nc] = True

ans = 0
for idx in range(len(cow_position)):
    visited = [[False for _ in range(n+1)] for _ in range(n+1)]
    # 소가 방문하지 못한 목초지는 visited에 False로 표시
    bfs(cow_position[idx][0], cow_position[idx][1])
    # 현재 탐색한 소 이후의 소들 중 방문하지 않은 목초지에 있는 소가 있으면 ans += 1
    for r,c in cow_position[idx+1:]:
        if not visited[r][c]:
            ans += 1
print(ans)    