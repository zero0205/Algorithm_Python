from collections import deque
import sys
input = sys.stdin.readline


def bfs(map_data):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[k+1]*m for _ in range(n)]  # 해당 칸까지 최단 거리로 올 때 부순 벽의 최소 개수
    visited[0][0] = 0
    q = deque([(0, 0, 1)])
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[x][y]+map_data[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]+map_data[nx][ny]
                    q.append((nx, ny, cnt+1))
    return -1


n, m, k = map(int, input().split())
map_data = []
for i in range(n):
    map_data.append(list(map(int, input().strip())))
print(bfs(map_data))
