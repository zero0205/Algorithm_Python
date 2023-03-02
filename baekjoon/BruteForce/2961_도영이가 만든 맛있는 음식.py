from itertools import combinations

n = int(input())
ingredient = []
for _ in range(n):
    ingredient.append(tuple(map(int, input().split())))

ans = int(1e9)
for i in range(1, n+1): # 재료 가짓수
    for arr in combinations(ingredient, i):
        sour = 1
        bitter = 0
        for s, b in arr:
            sour *= s
            bitter += b
        ans = min(ans, abs(sour-bitter))
print(ans)