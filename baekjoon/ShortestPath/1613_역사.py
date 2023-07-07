import sys
input = sys.stdin.readline

INF = int(1e9)

n, k = map(int, input().split())
dist = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    dist[a][b] = 1

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > (dist[i][k] + dist[k][j]):
                dist[i][j] = (dist[i][k] + dist[k][j])
    
s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if dist[a][b] != INF:
        print(-1)
    elif dist[b][a] != INF:
        print(1)
    else:
        print(0)