import sys
input = sys.stdin.readline
from collections import deque

horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
monkey = [(-1, 0), (0, 1), (1, 0), (0, -1)]

INF = int(1e9)

k = int(input())
w, h = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

q = deque([(0, 0, k, 0)])
visited = [[[False]*(k+1) for _ in range(w)]  for _ in range(h)]    # 점프 k번 남았을때 방문 여부
visited[0][0][k] = True
ans = INF
while q:
    x, y, remain_k, cnt = q.popleft()
    if x == h-1 and y == w-1:
        print(cnt)
        exit()
    # k 잔여 횟수 남아있을때
    if remain_k > 0:
        for dx, dy in horse:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == 0 and not visited[nx][ny][remain_k-1]:
                    q.append((nx, ny, remain_k-1, cnt+1))
                    visited[nx][ny][remain_k-1] = cnt+1
    for dx, dy in monkey:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] == 0 and not visited[nx][ny][remain_k]:
                q.append((nx, ny, remain_k, cnt+1))
                visited[nx][ny][remain_k] = cnt+1
print(-1)     