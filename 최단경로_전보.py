import heapq

INF = int(1e9)

# n : 도시의 개수, m : 통로의 개수, c : 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]  # 연결된 노드 정보들을 저장
distance = [INF] * (n + 1)  # 최단 거리 테이블. 모두 무한으로 초기화

# 통로에 대한 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z)) # x -> y로 가는 비용이 z
    
# 개선된 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, 1))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:    # 이미 처리된 노드
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행                
dijkstra(c)

city = 0
time = 0

for i in distance:
    if i != INF and i != 0:
        city += 1
        time = max(time, i)
        
print(city, time)