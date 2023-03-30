import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
road = [[int(1e9)] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    road[a][b] = l
    road[b][a] = l

for i in range(n+1):
    road[i][i] = 0  # 자기 자신으로 가는 경로는 0으로 초기화
    
# 플로이드-워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if road[i][j] > road[i][k] + road[k][j]:
                road[i][j] = road[i][k] + road[k][j]    # 더 짧은 경로로 갱신
    
ans = 0            
for start in range(1, n+1):
    item_sum = 0
    for i in range(1, n+1):
        if road[start][i] <= m:
            item_sum += items[i]
    ans = max(ans, item_sum)

print(ans)