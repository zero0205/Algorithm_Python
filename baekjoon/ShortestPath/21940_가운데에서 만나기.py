n, m = map(int, input().split())
road = [[int(1e9)] * (n+1) for _ in range(n+1)]
for i in range(n+1):    # 초기화
    road[i][i] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    road[a][b] = t  # 도시 a -> 도시 b로 가는데 걸리는 시간 t
k = int(input())
cities = list(map(int, input().split()))    # 준형이와 친구들이 살고 있는 도시들

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if road[i][j] > (road[i][k]+road[k][j]):
                road[i][j] = road[i][k]+road[k][j]

# 왕복시간이 최소가 되는 도시 찾기
ans = []
min_time = int(1e9)
for x in range(1, n+1):
    tmp = 0
    for c in cities:
        tmp = max(road[c][x]+road[x][c], tmp)

    if tmp < min_time:
        ans = [x]
        min_time = tmp
    elif tmp == min_time:
        ans.append(x)

print(*ans)
