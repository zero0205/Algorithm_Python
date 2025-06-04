from collections import deque

n, m = map(int, input().split())
maze = []
start = []
for i in range(n):
    line = list(input())
    for j in range(m):
        if line[j] == "0":
            start = [i, j]
            line[j] = "."
    maze.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([[*start, 0, frozenset()]])
visited = set()

while q:
    x, y, d, keys = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            new_keys = keys
            can_move = False
            if maze[nx][ny] == ".":  # 빈 칸
                can_move = True
            elif maze[nx][ny].isalpha() and maze[nx][ny].islower():  # 열쇠 획득
                new_keys = keys | {maze[nx][ny]}
                can_move = True
            elif maze[nx][ny].isalpha() and maze[nx][ny].isupper() and maze[nx][ny].lower() in keys:    # 문 열고 이동
                can_move = True
            elif maze[nx][ny] == "1":
                print(d+1)
                exit()

            if can_move and (nx, ny, new_keys) not in visited:
                q.append([nx, ny, d+1, new_keys])
                visited.add((nx, ny, new_keys))

print(-1)
