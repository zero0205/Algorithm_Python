from collections import deque

INF = int(1e9)

def bfs(board):
    n = len(board)
    arr = [[[INF] * 2 for _ in range(n)] for _ in range(n)]
    # 방향 인덱스 2 미만이면 가로, 이상이면 세로
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 방향 0은 가로, 1은 세로
    # 행, 열, 방향 순서
    q = deque([(0,0,0), (0,0,1)])
    arr[0][0][0] = 0    # 가로 방향에서 온 경우
    arr[0][0][1] = 0    # 세로 방향에서 온 경우
    while q:
        x, y, d= q.popleft()   # 행, 열, 방향
        if x == n -1 and y == n - 1:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = 0 if i < 2 else 1
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                cost = 0 if d == nd else 500
                if arr[x][y][d] + 100 + cost < arr[nx][ny][nd]:
                    arr[nx][ny][nd] = arr[x][y][d] + 100 + cost
                    q.append((nx, ny, nd))
    return min(arr[n-1][n-1])

def solution(board):
    answer = bfs(board)
    return answer

# 테스트 케이스
print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
print(solution([[0,0,0,0,0,0,0,0], [1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]]))