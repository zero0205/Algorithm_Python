n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:   # k번째 노드를 거쳐서 갈 수 있는 경우
                graph[i][j] = 1

for r in range(n):
    print(*graph[r])