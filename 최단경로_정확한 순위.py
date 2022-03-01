# 플로이드 워셜 알고리즘을 적용하여 최단거리가 구해지는 학생들의 수를 구하자
# 학생들의 수 n, 두 학생의 성적 비교 횟수 m 입력받기
n, m = map(int, input().split()) 

# 플로이드 워셜 적용을 위한 그래프 초기화
INF = int(1e9)  # 무한값으로 10억 사용
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):  # 자기 자신으로 가는 건 0으로 초기화
    graph[i][i] = 0
# 두 학생의 성적 비교 결과 입력 받기 (A < B)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
# 플로이드 워셜 알고리즘
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
        
    
# 나보다 높은 사람 명수 + 낮은 사람 명수 = n - 1이면 등수 알 수 있음
answer = 0
for student in range(1, n + 1):
    high = 0
    low = 0
    # 나보다 높은 사람은 같은 행에서
    for c in graph[student]:
        if c == 0 or c >= INF:
            continue
        high += 1
    # 나보다 낮은 사람은 같은 열에서
    for r in range(1, n + 1):
        if graph[r][student] == 0 or graph[r][student] >= INF:
            continue    
        low += 1
    # 둘이 합해서 n - 1이면 answer++
    if (high + low) == (n - 1):
        answer += 1
        
print(answer)
    
##### test case ####
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4