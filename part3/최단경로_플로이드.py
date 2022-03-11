import sys
input = sys.stdin.readline

INF = int(1e9)  # 무한값
# 도시의 개수 n 입력받기
n = int(input())
# 버스의 개수 m 입력받기
m = int(input())
# 최단 거리 저장하기 위한 그래프. 값은 모두 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 본인에서 본인으로 가는 경로는 0으로 초기화
for i in range(n + 1):
    graph[i][i] = 0
# 버스 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a: 시작 도시, b: 도착 도시, c: 비용
    graph[a][b] = min(graph[a][b], c)  # a->b 로 갈 때 필요한 비용 c
    
# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])
            
# 최단 거리 출력
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if graph[r][c] == INF:
            print(0, end=" ")
        else:
            print(graph[r][c], end=" ")
    print()