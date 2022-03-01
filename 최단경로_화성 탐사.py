INF = int(1e9)  # 무한을 나타내는 값으로 10억 사용
dir = [(-1,0),(1,0),(0,-1),(0,1)]   # 상하좌우
# 테스트 케이스 개수 t 입력
# t = int(input())
# 테스트 케이스별 수행
# for _ in range(t):
# 맵의 크기 n 입력
n = int(input())
# 맵정보 입력받기
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().split())))
    
# 이미 방문한 칸 체크용
visited = [[-1] * n for _ in range(n)]
visited[0][0] = map_data[0][0]    # 처음 시작 위치의 값 초기화

row = 0
col = 0

while True:
    q = []
    for d in dir:
        nr = row + d[0]
        nc = col + d[1]
        # 범위를 벗어나는지 체크
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        # 이미 방문한 칸인지 체크
        if visited[nr][nc] != -1:
            continue
        # 큐에 넣기
        q.append((map_data[nr][nc], nr, nc))    # (비용, 행, 열)
    # q의 값들 정렬(비용 기준으로)
    q.sort(key=lambda x: (x[0],-x[1],-x[2]))
    # print(q)
    nr, nc, cost = q[0][1], q[0][2], q[0][0]
    visited[nr][nc] = visited[row][col] + cost
    # print(visited[nr][nc])
    row = nr
    col = nc
    # [N-1][N-1] 칸에 도착했다면 빠져나오기
    if row == (n-1) and col == (n-1):
        break
print(visited[n-1][n-1])
    
#### test case ####
# 3

# 3
# 5 5 4
# 3 9 1
# 3 2 7

# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0 
# 3 6 5 1 5

# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4