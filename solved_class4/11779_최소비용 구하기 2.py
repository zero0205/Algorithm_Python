import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
bus = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split()) # 출발, 도착, 비용
    bus[s].append((e, c))
start, dest = map(int, input().split())

d = [INF] * (n + 1) # 출발점에서 각 노드로 가는 최소 비용 저장할 리스트
d[start] = 0
route = [[] for _ in range(n + 1)]  # 경로
route[start].append(start)
    
def dijkstra(start):
    q = [(0, start)]

    while q:
        cost, now = heapq.heappop(q)
        if d[now] < cost : # 원래 저장된 값이 더 작다면 이미 방문한 노드
                continue
        # 인접 노드들 확인
        for next_n, next_c in bus[now]:
            next_cost = cost + next_c  # 현재 노드를 거쳐 다음 노드로 가는 비용
            if next_cost < d[next_n]:  # 현재 노드를 거치는게 더 최단거리인 경우
                d[next_n] = next_cost
                heapq.heappush(q, (next_cost, next_n))
                route[next_n] = []
                for r in route[now]:
                    route[next_n].append(r)
                route[next_n].append(next_n)
                
dijkstra(start)
print(d[dest])
print(len(route[dest]))
print(' '.join(map(str,route[dest])))