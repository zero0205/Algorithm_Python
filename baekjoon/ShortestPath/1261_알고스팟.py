from heapq import heappop, heappush

m, n = map(int, input().split())
maze = [input() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

break_num = [[n*m]*m for _ in range(n)]
break_num[0][0] = 0
q = []
heappush(q, (0, 0, 0))
while q:
    cnt, x, y = heappop(q)
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            next_cnt = cnt + (1 if maze[nx][ny] == '1' else 0)
            if break_num[nx][ny] > next_cnt:
                break_num[nx][ny] = next_cnt
                heappush(q, (next_cnt, nx, ny))

print(break_num[n-1][m-1])
