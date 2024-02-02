from collections import deque

move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

for _ in range(int(input())):
    l = int(input())
    sx, sy = map(int, input().split())
    dx, dy = map(int, input().split())

    q = deque([(sx, sy, 0)])
    visited = [[False]*l for _ in range(l)]
    visited[sx][sy] = True
    while q:
        x, y, cnt = q.popleft()
        if x == dx and y == dy:
            print(cnt)
            break
        for i in range(8):
            nx = x+move[i][0]
            ny = y+move[i][1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True
