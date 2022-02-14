from collections import deque

n, m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

deq = deque([(0,0)])

# 아직 방문 안 한 노드면 큐에 넣고 
def bfs():
  while deq:
    x, y = deq.popleft()
    # 상하좌우로 이동가능한지 탐색
    # 이동 가능한 칸은 큐에 넣어주고 거기까지의 거리로 값을 변경
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 안에 있는지?
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 갈 수 있는 칸이면 그 칸까지의 거리를 넣어줌. 이미 지나온 칸이면 값이 1이 아닐것
      if graph[nx][ny] == 1:
        deq.append((nx,ny))
        graph[nx][ny] = graph[x][y] + 1

bfs()    

print(graph[n-1][m-1])