from collections import deque
from heapq import heappop, heappush

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
island_info = [[-1]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, num):  # 섬 구분
    q = deque([(x, y)])
    island_info[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 같은 섬의 아직 방문 안 한 땅인 경우
                if board[nx][ny] == 1 and island_info[nx][ny] == -1:
                    q.append((nx, ny))
                    island_info[nx][ny] = num


def bfs2(x, y):    # 섬끼리 다리 내리기
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 같은 섬의 아직 방문 안 한 땅인 경우
                if board[nx][ny] == 1 and not visited:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                # 바다인 경우 => 다리 내려보기
                if board[nx][ny] == 0:
                    bridge(nx, ny, i)


def bridge(x, y, d):
    cnt = 1
    nx, ny = x, y
    s = island_info[x-dx[d]][y-dy[d]]
    while True:
        nx += dx[d]
        ny += dy[d]
        cnt += 1
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return
        # 땅에 닿음
        if board[nx][ny] == 1:
            # 다른 섬에 거리 2 이상 다리 건설 가능
            if s != island_info[x][y] and cnt-1 >= 2:
                e = island_info[nx][ny]
                if (cnt-1, s, e) not in graph:
                    heappush(graph, (cnt-1, s, e))
            return


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a == b:  # 사이클 형성
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


# 섬 구분
island_num = 1
for i in range(n):
    for j in range(m):
        # 아직 방문 안한 섬 -> bfs 수행
        if board[i][j] == 1 and island_info[i][j] == -1:
            bfs(i, j, island_num)
            island_num += 1

# 다리 내리기
graph = []  # 섬끼리 거리
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            bfs2(i, j)

# MST 구성
ans = 0
connect = 0  # 섬들간 연결의 개수
parent = [i for i in range(island_num+1)]
while graph:
    dist, s, e = heappop(graph)
    if union_parent(s, e, parent):
        ans += dist
        connect += 1

print(ans if connect == island_num-2 else -1)
