from collections import deque

def bfs(x,y,m,n,idx):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x,y)])
    m[x][y] = idx # 방문 처리
    idx += 1
    now_x, now_y = x, y 

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if m[nx][ny] == 0:
                    q.append((nx, ny))
                    m[nx][ny] = idx   # 방문 처리
                    idx += 1
    return [now_x, now_y, idx]

def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1
    idx = 2
    nx, ny = 0, 0
    for i in range(2, n + 1):
        if horizontal:  # 수평
            nx += 0
            ny += 1
            horizontal = False
        else:
            nx += 1
            ny += 0
            horizontal = True
        nx, ny, idx = bfs(nx,ny,answer,i,idx)
        print(nx, ny, idx)
    print()
    for r in answer:
        for c in r:
            print(c, end=" ")
        print()
    return answer
