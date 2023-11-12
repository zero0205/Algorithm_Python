from collections import deque

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for i in range(n):
    board.append(input())

q = deque([(0, 0)])
# 아직 방문 안한 방: INF, 방문한 방: 이 방까지 오는데 없앤 최소 검은 방 수
visited = [[INF]*n for _ in range(n)]
visited[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[x][y] < visited[nx][ny]:
            q.append((nx, ny))
            # 흰 방
            if board[nx][ny] == '1':
                visited[nx][ny] = visited[x][y]
            # 검은 방
            else:
                visited[nx][ny] = visited[x][y] + 1
print(visited[n-1][n-1])
