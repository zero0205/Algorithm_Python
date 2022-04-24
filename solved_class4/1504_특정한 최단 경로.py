# https://www.acmicpc.net/problem/1504

import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

# n : 정점의 개수 / e : 간선의 개수
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distances = [[INF] * (n + 1) for _ in range(3)]
for _ in range(e):
    # a에서 b까지 거리가 c인 양방향 길 존재 
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
    
def dijkstra(idx, start):
    q = []
    heapq.heappush(q, (0, start))
    distances[idx][start] = 0 # 초기화
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 방문했으면 무시
        if distances[idx][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거치는 경우가 더 짧은 경우
            if cost < distances[idx][i[0]]:
                distances[idx][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
lst = [1, v1, v2]
for idx in range(3):
    dijkstra(idx, lst[idx])

# 1 -> v1 -> v2 -> n
path1 = distances[0][v1] + distances[1][v2] + distances[2][n]
# 1 -> v2 -> v1 -> n
path2 = distances[0][v2] + distances[2][v1] + distances[1][n]
ans = min(path1, path2)
if ans < INF:
    print(ans)
else:
    print(-1)
