# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))
    
# 집, 치킨집 위치 파악
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1: # 집
            house.append((i, j))
            continue
        if city[i][j] == 2: # 치킨집
            chicken.append((i, j))
# 남길 치킨집 리스트
alive = list(combinations(chicken, m))

min_sum = int(1e9)
for lst in alive:
    sum = 0
    for h in house:
        min_chicken = int(1e9)
        # 각 집의 치킨 거리 계산
        for c in lst:
            min_chicken = min(min_chicken, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        sum += min_chicken
    min_sum = min(min_sum, sum)

print(min_sum)