from collections import deque


def solution(grid):
    answer = 1
    n = len(grid)

    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([(0, 0, 2)])
    visited = [[0]*n for _ in range(n)]  # 각 방향대로 0000. 이미 방문 했으면 1
    visited[0][0] = 4
    while q:
        x, y, d = q.popleft()
        if grid[x][y] == 'R':
            d = (d+1) % 4
        elif grid[x][y] == 'L':
            d = (d-1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            d = (d+2) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        if visited[nx][ny] & (1 << d) == 0:
            if visited[nx][ny] == 0:
                answer += 1
            q.append((nx, ny, d))
            visited[nx][ny] |= (1 << d)
    return answer
