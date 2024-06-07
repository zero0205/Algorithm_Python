from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    q = deque()
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]
    dest = []
    cube = [[] for _ in range(l)]
    for i in range(l):
        for j in range(r):
            row = input()
            for k in range(c):
                if row[k] == 'S':   # 시작점
                    visited[i][j][k] = True
                    q.append((i, j, k, 0))
                elif row[k] == 'E':  # 출구
                    dest = [i, j, k]
            cube[i].append(row)
        tmp = input()
    ans = -1
    # BFS
    while q:
        x, y, z, cnt = q.popleft()
        if [x, y, z] == dest:
            ans = cnt
            break
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and not visited[nx][ny][nz] and cube[nx][ny][nz] != '#':
                q.append((nx, ny, nz, cnt+1))
                visited[nx][ny][nz] = True
    print(f"Escaped in {ans} minute(s)." if ans != -1 else "Trapped!")
