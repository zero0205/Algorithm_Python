####### 플로이드 워셜은 시간초과!! #######
# import sys
# input = sys.stdin.readline

# INF = int(1e9)

# n, m, x = map(int, input().split())

# road = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
# for i in range(n + 1):
#     road[i][i] = 0  # 자기 자신으로 가는 길은 0으로 초기화
    
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     road[s][e] = t
    
# # 플로이드 워셜  
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             road[i][j] = min(road[i][j], road[i][k] + road[k][j])
            
# answer = 0
# for c in range(1, n + 1):
#     answer = max(answer, road[x][c] + road[c][x])

# print(answer)

###########################################################
import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

n, m, x = map(int, input().split())

road = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    road[s].append((e, t))

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    # 자기자신으로 가는 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:    # 이미 처리된 노드
            continue
        for e, t in road[now]:
            cost = dist + t
            # 현재 노드를 거치는게 더 짧은 경로일 경우
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))
                
    return distance

# 각 마을의 학생들이 x번 마을을 오고 가는 값 중 최댓값 구하기
answer = 0
x_to_each = dijkstra(x)

for i in range(1, n + 1):
    if i == x:
        continue
    answer = max(answer, x_to_each[i] + dijkstra(i)[x])
    
print(answer)