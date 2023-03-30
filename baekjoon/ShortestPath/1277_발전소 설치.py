import sys
input = sys.stdin.readline
from heapq import heappop, heappush
from math import sqrt, floor

n, w = map(int, input().split())
m = float(input())  # 제한 길이

plants = [[]]
for _ in range(n):  # 1~N번 발전소의 위치
    plants.append(list(map(int, input().split())))
    
def get_distance(a, b):
    x = plants[a][0]-plants[b][0]
    y = plants[a][1]-plants[b][1]
    return sqrt(x**2 + y**2)

wire = [[] for _ in range(n+1)]
for _ in range(w):
    a, b = map(int, input().split())
    # 남아있는 전선들은 추가 길이에 계산되지 않도록 0으로 설정
    wire[a].append((b, 0))
    wire[b].append((a, 0))

# 발전소들 간의 거리 계산
for i in range(1, n+1):
    for j in range(i+1, n+1):
            dist = get_distance(i, j)
            if dist <= m:   # 제한 길이 넘는지 확인
                wire[i].append((j, dist))
                wire[j].append((i, dist))

# 다익스트라
q = []
heappush(q, (0, 1)) # 1번 발전소(출발점) heapq에 넣어주기
dp = [int(1e9)] * (n+1)
dp[1] = 0
while q:
    dist, now = heappop(q)
    if dp[now] < dist:
        continue
    for nx, nd in wire[now]:
        next_dist = dist + nd
        if dp[nx] > next_dist:
            dp[nx] = next_dist
            heappush(q, (next_dist, nx))

print(floor(dp[n]*1000))