from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
points = []
for i in range(n):
    row = list(input())
    maze.append(row)
    for j in range(n):
        if row[j] == 'S' or row[j] == 'K':
            maze[i][j] = len(points)
            points.append((i, j))

# BFS
graph = []


def bfs(idx):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    x, y = points[idx]
    q = deque([(x, y, 0)])
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '1':
                q.append((nx, ny, cnt+1))
                visited[nx][ny] = True
                if maze[nx][ny] != '0':
                    graph.append((cnt+1, idx, maze[nx][ny]))


for i in range(len(points)):
    bfs(i)

# MST(Kruskal Algorithm)
parent = [i for i in range(len(points))]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


graph.sort()
ans = 0
num = 0
for dist, s, e in graph:
    if union_parent(s, e):
        ans += dist
        num += 1
    if num >= len(points)-1:
        break

print(ans if num == len(points)-1 else -1)
