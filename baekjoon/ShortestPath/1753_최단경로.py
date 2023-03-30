import sys, heapq
input = sys.stdin.readline

vertex, edge = map(int, input().split())
k = int(input())
graph = [[] for _ in range(vertex+1)]
for _ in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라
q = []
dp = [int(1e9)] * (vertex+1)

heapq.heappush(q, (0, k))   # 시작점 heapq에 넣기
dp[k] = 0
while q:
    weight, now = heapq.heappop(q)
    for nx, nw in graph[now]:
        if dp[nx] > weight + nw:    # nx를 거쳐 가는게 더 짧은 경로인 경우
            dp[nx] = weight + nw
            heapq.heappush(q, (weight+nw, nx))
        
for i in dp[1:]:
    print("INF" if i == int(1e9) else i)