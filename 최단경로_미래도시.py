# n : 전체 회사의 개수, m : 경로의 개수
n, m = map(int, input().split())

# 최단 거리 테이블 초기화
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(n + 1):
    graph[a][a] = 0
    
# 연결된 두 회사의 번호들 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# x : 2번째 찾아감, k : 1번째 찾아감
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 적용
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 1 -> k -> x 이동하는 값 출력
cost = graph[1][k] + graph[k][x]
if cost >= INF:
    print(-1)
else:
    print(cost)