from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, group_num):
    res = 1
    q = deque([(x, y)])
    matrix[x][y] = group_num
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x+dx[i]
            ny = now_y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                q.append((nx, ny))
                matrix[nx][ny] = group_num
                res += 1
    return res


group_num = 2
group = dict()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            size = bfs(i, j, group_num)
            group[group_num] = size
            group_num += 1

answer = 0
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 0:
            cnt = 1
            visited_group = set([0])
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] not in visited_group:
                    group_num = matrix[nx][ny]
                    cnt += group[group_num]
                    visited_group.add(group_num)
            answer = max(answer, cnt)
print(answer)
