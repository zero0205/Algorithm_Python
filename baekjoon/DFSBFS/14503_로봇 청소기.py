########## DFS ###########
n, m = map(int, input().split())
# 로봇 위치 (r, c), d는 방향(0:북, 1:동, 2:남, 3:서)
r, c, d = map(int, input().split())
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))
 
cleaned = [[False for _ in range(m)] for _ in range(n)]
cleaned[r][c] = True
 
# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
 
ans = 1
 
def dfs(x, y, dir):
    global ans    
 
    for i in range(1, 5):
        nd = (dir - i) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if not cleaned[nx][ny] and map_data[nx][ny] == 0:
            cleaned[nx][ny] = True
            ans += 1
            dfs(nx, ny, nd)
            return
    # 4방향 모두 청소되어 있거나 벽인 경우
    bd = (dir + 2) % 4
    bx = x + dx[bd]
    by = y + dy[bd]
    if map_data[bx][by] == 1: # 후진 불가
        return
    dfs(bx, by, dir)
    
dfs(r, c, d)
print(ans)

############### BFS ###############
# from collections import deque
 
# n, m = map(int, input().split())
# # 로봇 위치 (r, c), d는 방향(0:북, 1:동, 2:남, 3:서)
# r, c, d = map(int, input().split())
# map_data = []
# for _ in range(n):
#     map_data.append(list(map(int, input().split())))
    
# visited = [[False for _ in range(m)] for _ in range(n)]
# visited[r][c] = True    # 방문 처리
 
# # 북동남서
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
 
# ans = 1
# q = deque([(r, c, d)])
# tmp = 0
 
# while q:
#     x, y, dir = q.popleft()
    
#     for i in range(4):
#         dir = (dir - 1) % 4
#         nx = x + dx[dir]
#         ny = y + dy[dir]
#         # 청소 가능한 경우
#         if not visited[nx][ny] and map_data[nx][ny] == 0:   
#             q.append((nx, ny, dir))
#             visited[nx][ny] = True
#             ans += 1
#             tmp = 0
#             break
#         else:
#             tmp += 1
#     # 4방향 모두 청소 불가한 경우
#     if tmp >= 4:
#         bx = x - dx[dir]
#         by = y - dy[dir]
#         if map_data[bx][by] == 1: # 후진 불가
#             break
#         q.append((bx, by, dir))
#         tmp = 0