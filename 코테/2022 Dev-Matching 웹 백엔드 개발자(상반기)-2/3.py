from collections import deque

def print_map(m):
    for r in m:
        for c in r:
            print(c, end=" ")
        print()

def bfs(x,y,m,r,c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    res = 1
    q = deque([(x,y)])
    m[x][y] = 2 # 방문 처리

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if m[nx][ny] == 0:
                    q.append((nx, ny))
                    m[nx][ny] = 2   # 방문 처리
                    res += 1
    return res

def solution(rows, columns, lands):
    answer = [-1, -1]
    map_data = [[0 for _ in range(columns)] for _ in range(rows)]
    for l in lands:
        map_data[l[0]-1][l[1]-1] = 1

    bfs(0,0,map_data,rows,columns)  # 바다 처리

    max_size = -1
    min_size = 100000
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if map_data[i][j] == 0:
                size = bfs(i,j,map_data,rows,columns)
                max_size = max(max_size, size)
                min_size = min(min_size, size)
    if max_size != -1 and min_size != -1:
        answer = [min_size, max_size]
    return answer
