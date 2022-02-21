import sys
from collections import deque
# n : 도시의 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시의 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [1000000] * (n + 1)  # 출발 도시로부터의 거리 저장할 배열

# a -> b로 이동하는 단방향 도로
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
visited = [False] * (n + 1) # 방문 여부

# def dfs(graph, v, visited, dist):
#     visited[v] = True
#     distance[v] = dist
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited, dist + 1)

# dist = 0 
# dfs(graph, x, visited, dist)

# answer = []
# for j in range(len(distance)):
#     if distance[j] == k:
#         answer.append(j)
        
# print(answer)

def bfs(graph, start, visited):
    que = deque([start])
    dist = 0
    distance[start] = 0
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while que:
        v = que.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                distance[i] = distance[v] + 1
                visited[i] = True

bfs(graph, x, visited)        
    
answer = []
for j in range(len(distance)):
    if distance[j] == k:
        answer.append(j)
        
answer.sort()
if answer:
    for j in answer:
        print(j)
else:
    print(-1)