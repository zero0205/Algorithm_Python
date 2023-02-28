from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

ans = 0
for comb in combinations(card, 3):
    if sum(comb) <= m:
        ans = max(ans, sum(comb))
    
print(ans)