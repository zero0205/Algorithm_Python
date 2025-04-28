import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
switchs = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switchs[(x, y)].append((a, b))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(1, 1)])
# 불이 켜진 방 체크
lights = [[False]*(n+1) for _ in range(n+1)]
lights[1][1] = True
# 방문 여부 체크
visited = [[False]*(n+1) for _ in range(n+1)]
visited[1][1] = True

while q:
    x, y = q.popleft()
    # 현재 방의 스위치로 다른 방 불 켜기
    for a, b in switchs[(x, y)]:
        if lights[a][b]:
            continue
        lights[a][b] = True
        # 지금 불을 켠 (a, b)가 방문이 가능한 곳인지 확인. 가능하다면 큐에 넣기
        for j in range(4):
            na = a+dx[j]
            nb = b+dy[j]
            if 0 < na <= n and 0 < nb <= n and visited[na][nb]:
                q.append((a, b))
                visited[a][b] = True
                break

    # 인접한 방으로 이동
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 < nx <= n and 0 < ny <= n and lights[nx][ny] and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True


result = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if lights[i][j]:
            result += 1

print(result)
