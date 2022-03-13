def solution(n, edges):
    # i -> k로 가는 경로는 반드시 j를 지남
    answer = 0
    INF = int(1e9)
    # 플로이드 워셜
    graph = [[INF] * n for _ in range(n)]

    # 자기 자신으로 가는 건 0으로 초기화
    for i in range(n):
        graph[i][i] = 0
    
    # 직접 연결된 간선들
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for row in range(n):
        for col in range(n):
            if not (graph[row][col] == INF or graph[row][col] == 0 or graph[row][col] == 1):
                answer += (graph[row][col] - 1)
    return answer