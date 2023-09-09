from collections import deque, defaultdict
from itertools import permutations

def solution(n, board):
    answer = [[]]
    alphabet = defaultdict(list)
    dx = [-1, 0, 1, 0]
    dy= [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            if board[i][j].isalpha():
                alphabet[board[i][j]].append((i, j))
    # 전선 연결 순서
    for perm in permutations(alphabet.keys(), len(alphabet)):
        visited = [[False]*n for _ in range(n)]
        connect2 = True
        answer = [[0]*n for _ in range(n)]
        for a in perm:
            start = alphabet[a][0]
            end = alphabet[a][1]
            q = deque([start]) # 시작
            visited[start[0]][start[1]] = True
            connect1 = False
            while q:
                x, y = q.popleft()
                if x == end[0] and y == end[1]:
                    connect1 = True
                    break
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and (board[nx][ny] == '.' or board[nx][ny] == a):
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            answer[x][y] += (2 ** d)
                            answer[nx][ny] += (2 ** ((d-2)%4))
            if not connect1:
                connect2= False
                break
        if connect2: # 모두 연결 가능
            break
    return answer

# print(solution(3, ["..d", ".##","..d"]))
# [[6, 10, 8], [5, 0, 0], [3, 10, 8]]
print(solution(5, [".....",".....", "..a..",".b.b.",".dad."]))
# [[6, 10, 10, 10, 12],[5, 6, 10, 12, 5],[5, 5, 4, 5, 5],[5, 1, 5, 1, 5],[3, 8, 1, 2, 9]]