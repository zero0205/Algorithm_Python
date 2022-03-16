# https://www.acmicpc.net/problem/1012

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 테스트 케이스 개수 t 입력
t = int(input())

for _ in range(t):
    # m: 배추밭 가로 ,n: 배추밭 세로 , k: 배추 개수
    m, n, k = map(int, input().split())
    field = [[False] * m for _ in range(n)] # 배추밭
    # 배추 심어진 위치 입력받아서 표시
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = True
    
    res = 0
    for row in range(n):
        for col in range(m):
            # BFS
            if field[row][col]:
                res += 1
                q = deque([(row, col)])
                field[row][col] = False # 방문 처리
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if field[nx][ny]:
                            q.append((nx, ny))
                            field[nx][ny] = False   # 방문 처리
    print(res)