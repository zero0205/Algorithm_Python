import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dist = [[int(1e9)] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    
# Floyd-Warshall
for k in range(1, v+1):
    for a in range(1,v+1):
        for b in range(1, v+1):
            if dist[a][b] > dist[a][k] + dist[k][b]:
                dist[a][b] = dist[a][k] + dist[k][b]
                
ans = int(1e9)
for i in range(1, v+1):
    ans = min(ans, dist[i][i])
    
print(ans if ans != int(1e9) else -1)