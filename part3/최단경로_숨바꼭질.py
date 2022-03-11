# 1번 헛간으로부터 다른 모든 헛간으로까지의 최단 경로를 구하고
# 그 중 가장 긴 거리를 가진 헛간을 선택
# 다익스트라 알고리즘 사용

import heapq

INF = int(1e9)  # 무한값
# 헛간 개수: n, 통로 개수: m
n, m = map(int, input().split())

# 연결된 정보를 저장하기 위한 리스트
graph = [[] for _ in range(n + 1)] 

# 1번 헛간으로부터 최단 거리 저장용. 무한값으로 초기화
distance = [INF] * (n + 1)
distance[1] = 0 # 1번에서 출발하니까
    
# 연결된 두 헛간
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 다익스트라 알고리즘
q = []  # 최소힙을 위한 리스트
now = 1 # 현재 노드
heapq.heappush(q, (0, now))
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:    # 이미 방문한 노드
        continue
    # 현재 노드와 연결된 다른 인접한 노드 확인
    for node in graph[now]:
        cost = dist + 1
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, (cost, node))

max_value = 0
max_distance = 0
same_dist = 0
for i in range(1, n + 1):
    if distance[i] > max_distance:
        max_distance = distance[i]
        max_value = i
        same_dist = 1
    elif distance[i] == max_distance:
        same_dist += 1

print(max_value, max_distance, same_dist)        

### test case ###
# 6 7
# 3 6
# 4 3 
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2