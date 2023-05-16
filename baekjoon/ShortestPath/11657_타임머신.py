import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
path = []
for _ in range(m):
    a, b, c = map(int, input().split()) # a->b로 이동하는데 걸리는 시간 c
    path.append((a, b, c))
    
dist = [INF] * (n+1)
dist[1] = 0     # 시작 노드(1)의 dist값은 0
for i in range(n):
    for a,b,c in path:
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            if i == n-1:    # n번째 수행인데 값이 또 갱신 -> 음의 사이클 존재
                print(-1)
                exit()
            
for d in dist[2:]:
    print(-1 if d == INF else d)