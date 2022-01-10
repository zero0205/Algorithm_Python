from collections import deque

n, m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

cnt = 2 # 시작 칸과 마지막 칸 포함

# 아직 방문 안 한 노드면 큐에 넣고 
def bfs(x, y):
    # 출구 도착?
    if x == n and y == m:
        return cnt
DFS/BFS_미로 탈출(미완)
