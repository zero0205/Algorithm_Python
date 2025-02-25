import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
path_table = [["-"]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t
    path_table[a][b] = b
    path_table[b][a] = a

for k in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if graph[start][end] > graph[start][k]+graph[k][end]:
                graph[start][end] = graph[start][k]+graph[k][end]
                path_table[start][end] = path_table[start][k]

for i in range(1, n+1):
    print(*path_table[i][1:])
