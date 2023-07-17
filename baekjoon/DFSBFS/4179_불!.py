from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c = map(int, input().rstrip().split())
maze = []
q = deque([])
for i in range(r):
    maze.append(list(input())) # #은 벽, .은 빈 공간, J는 지훈이 초기 위치, F는 불
    for j in range(c):
        if maze[i][j] == 'J':
            q.appendleft((i, j, 0, False))
        elif maze[i][j] == 'F':
            q.append((i, j, 0, True))

while q:
    x, y, t, is_fire = q.popleft()
    if (x == 0 or x == r-1 or y == 0 or y == c-1) and maze[x][y] != 'F' and not is_fire:    # 탈출
        print(t+1)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#':
            if maze[nx][ny] == '.' and not is_fire: # 지훈이
                q.append((nx, ny, t+1, False))
                maze[nx][ny] = 'V'
            elif is_fire and maze[nx][ny] != 'F':   # 불 확산
                maze[nx][ny] = 'F'
                q.append((nx, ny, t+1, True))
    
print("IMPOSSIBLE")