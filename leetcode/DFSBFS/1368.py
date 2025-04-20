from collections import deque


def minCost(grid):
    n = len(grid)
    m = len(grid[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count = [[int(1e9)]*m for _ in range(n)]
    count[0][0] = 0
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 여기서 방향 바꿈
                if i != grid[x][y]-1 and count[x][y]+1 < count[nx][ny]:
                    q.append((nx, ny))
                    count[nx][ny] = count[x][y]+1
                # 방향 안 바꿈
                elif i == grid[x][y]-1 and count[x][y] < count[nx][ny]:
                    q.append((nx, ny))
                    count[nx][ny] = count[x][y]

    return count[n-1][m-1]


# print(minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))   # 3
print(minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))   # 0
# print(minCost([[1, 2], [4, 3]]))   # 1
