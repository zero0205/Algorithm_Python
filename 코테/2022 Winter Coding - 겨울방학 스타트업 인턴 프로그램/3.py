from collections import deque

def next_dir(x, y, now_dir):
    # 북쪽부터 시계방향으로 1~8
    dir = [(x-1, y-1, 8), (x-1, y, 1), (x-1, y+1, 2), (x, y+1, 3), (x+1, y+1, 4),
            (x+1, y, 5), (x+1, y-1, 6), (x, y-1, 7)]
    return [dir[(now_dir-1 + i)%8] for i in range(3)]

def solution(worldmap):
    n = len(worldmap)
    m = len(worldmap[0])

    q = deque([(0, 0, 3, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    # BFS
    while q:
        x, y, d, t = q.popleft()
        if x == n - 1 and y == m - 1:
            return t
        next_list = next_dir(x,y,d)
        for nx, ny, nd in next_list:
            # 지도를 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동 가능한 경우
            if worldmap[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx, ny, nd, t+1))
                visited[nx][ny] = True