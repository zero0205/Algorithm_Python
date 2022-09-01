import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append(input())
    
ans = 1

def bfs():
    global ans 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = set([(0, 0, board[0][0])])

    while q:
        x, y, route = q.pop()
        ans = max(ans, len(route))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in route:
                q.add((nx, ny, route + board[nx][ny]))

bfs()
print(ans)

#############################################
# import sys
# input = sys.stdin.readline

# r, c = map(int, input().split())

# board = []
# for _ in range(r):
#     board.append(input())
    
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# visited = set([board[0][0]])

# ans = 0

# def dfs(x, y, num):
#     global ans
#     ans = max(ans, num)
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 보드의 범위를 벗어나지 않고 아직 나오지 않은 알파벳이라면 계속 탐색
#         if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in visited:
#             visited.add(board[nx][ny])
#             dfs(nx, ny, num+1)
#             visited.remove(board[nx][ny])
# dfs(0,0,1)
# print(ans)