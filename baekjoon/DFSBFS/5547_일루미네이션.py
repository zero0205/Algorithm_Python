from collections import deque

w, h = map(int, input().split())
map_data = []
map_data.append([0] * (w+2))
for i in range(h):
    map_data.append([0] + list(map(int, input().split())) + [0])
map_data.append([0] * (w+2))
    
q = deque([(0, 0)])
visited = [[False] * (w+2) for _ in range(h+2)]
visited[0][0] = True
cnt = 0
while q:
    now_r, now_c = q.popleft()
    if now_r % 2 == 1:
        dir = [(-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)]
    else:
        dir = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for i in range(6):
        nr = now_r + dir[i][0]
        nc = now_c + dir[i][1]
        if 0 <= nr < h+2 and 0 <= nc < w+2:
            if map_data[nr][nc] == 0 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
            elif map_data[nr][nc] == 1:
                cnt += 1
print(cnt)         