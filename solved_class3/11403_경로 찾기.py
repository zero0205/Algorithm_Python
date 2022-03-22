# https://www.acmicpc.net/problem/11403

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = (1 if (graph[i][k] == 1 and graph[k][j] == 1) else 0)
                
# 출력
for row in graph:
    for el in row:
        print(el, end=' ')
    print()