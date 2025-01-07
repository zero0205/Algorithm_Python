answer = 64

n, m = map(int, input().split())
office = []
cctv = []
blank = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] != 0 and line[j] != 6:
            cctv.append([i, j, line[j]])
        elif line[j] == 0:
            blank += 1
    office.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 종류에 따라서 이동 가능한 경우의 수
dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


def move(x, y, dir_list):   # dir_list에 있는 모든 방향으로 최대한 이동
    visited = []
    for d in dir_list:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                visited.append((nx, ny))
                office[nx][ny] = 9
    return visited


def undo_move(visited):  # 이동하며 표시했던 것을 원래대로 되돌리기
    for x, y in visited:
        office[x][y] = 0


def dfs(idx, blank):
    global answer
    if idx == len(cctv):    # 모든 cctv를 다 시뮬레이션해봤을 때
        answer = min(answer, blank)
        return
    for dir_list in dir[cctv[idx][2]]:
        visited = move(cctv[idx][0], cctv[idx][1], dir_list)
        dfs(idx+1, blank-len(visited))
        undo_move(visited)


dfs(0, blank)
print(answer)
