# https://www.acmicpc.net/problem/1389

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

dist = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1
    
# 자기 자신으로 가는 거리는 0
for i in range(n + 1):
    dist[i][i] == 0
# 플로이드 워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
            
answer = 0
min_value  = INF
for i in range(1, n + 1):
    if min_value > sum(dist[i][1:]):
        min_value = sum(dist[i][1:])
        answer = i
print(answer)