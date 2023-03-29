import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    
# 다익스트라
distance = [int(1e9)] * (n+1)
distance[x] = 0
hq = []
heapq.heappush(hq, (0, x))
while hq:
    dist, now = heapq.heappop(hq)
    if distance[now] < dist:    # 이미 방문한 경우
        continue
    for nx in road[now]:
        if dist + 1 < distance[nx]:
            distance[nx] = dist + 1
            heapq.heappush(hq, (dist+1, nx))

flag = False        
for j in range(1, n+1):
    if distance[j] == k:
        flag = True
        print(j)
if not flag:
    print(-1)