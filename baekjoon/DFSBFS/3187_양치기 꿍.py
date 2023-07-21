from collections import deque

r, c = map(int, input().split())
farm = []
for _ in range(r):
    farm.append(list(input()))
  
def bfs(x, y):
    sheep, wolf = 0, 0
    if farm[x][y] == 'v':
        wolf += 1
    elif farm [x][y] == 'k':
        sheep += 1
        
    q = deque([(x, y)])
    farm[x][y] = '#'
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and farm[nx][ny] != '#':
                if farm[nx][ny] == 'v': # 늑대
                    wolf += 1
                elif farm[nx][ny] == 'k': # 양
                    sheep += 1
                q.append((nx, ny))
                farm[nx][ny] = '#'  # 방문한 칸 울타리로 표시
    # 양이 살아남으면 0, 늑대가 살아남으면 1
    return [0, sheep] if (sheep > wolf) else [1, wolf]

s, w = 0, 0
for i in range(r):
    for j in range(c):
        if farm[i][j] != '#':
            res, num = bfs(i, j)
            if res == 0:
                s += num
            else:
                w += num

print(s, w)