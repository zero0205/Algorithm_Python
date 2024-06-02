from collections import deque
import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
s = [0]+list(map(int, input().split()))
board = [list(input()) for _ in range(n)]
ans = [0]*(p+1)

castle = [deque() for _ in range(p+1)]
# 처음 성의 위치
for i in range(n):
    for j in range(m):
        if board[i][j] != '.' and board[i][j] != '#':
            castle[int(board[i][j])].append((i, j))
            ans[int(board[i][j])] += 1

# BFS
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    is_end = True
    for player in range(1, p+1):
        if not castle[player]:
            continue
        q = castle[player]
        for _ in range(s[player]):  # 한 턴에 이동할 수 있는 거리
            if not q:   # 더이상 이동 가능한 칸이 없는 경우
                break
            for _ in range(len(q)):
                x, y = q.popleft()
                for d in range(4):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                        board[nx][ny] = str(player)
                        q.append((nx, ny))
                        ans[player] += 1
                        is_end = False
    if is_end:
        break


print(*ans[1:])
