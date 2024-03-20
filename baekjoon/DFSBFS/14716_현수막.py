from collections import deque

m, n = map(int, input().split())
input_data = [list(map(int, input().split())) for _ in range(m)]

move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
visited = [[False]*n for _ in range(m)]
char_num = 0
for i in range(m):
    for j in range(n):
        if input_data[i][j] == 1 and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(8):
                    nx = x+move[d][0]
                    ny = y+move[d][1]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and input_data[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            char_num += 1
print(char_num)
